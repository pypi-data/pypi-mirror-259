<script lang="ts">
    import type { FileData } from "@gradio/client";
    import { BlockLabel } from "@gradio/atoms";
    import { File } from "@gradio/icons";
    import { onMount } from "svelte";
    // import * as SPLAT from "gsplat";
    import * as SPLAT from "https://cdn.jsdelivr.net/npm/gsplat@latest";
    import type { I18nFormatter } from "@gradio/utils";

    export let value: FileData[] | null;
    export let label = "";
    export let show_label: boolean;
    export let i18n: I18nFormatter;
    export let zoom_speed = 1;
    export let pan_speed = 1;

    let canvas: HTMLCanvasElement;
    let scene: SPLAT.Scene;
    let camera: SPLAT.Camera;
    let renderer: SPLAT.WebGLRenderer | null = null;
    let controls: SPLAT.OrbitControls;
    let mounted = false;
    let loading = false;

    // NEW CHANGE
    let currFrameIndex = 0;
    let currTime = Date.now();
    let NUM_FRAMES = 14;
    var frameIndexToObject = {};

    function reset_scene(): void {
        if (renderer !== null) {
            renderer.dispose();
            renderer = null;
        }

        scene = new SPLAT.Scene();
        camera = new SPLAT.Camera();
        renderer = new SPLAT.WebGLRenderer(canvas);
        controls = new SPLAT.OrbitControls(camera, canvas);
        controls.zoomSpeed = zoom_speed;
        controls.panSpeed = pan_speed;

        if (!value) {
            return;
        }

        const load = async () => {
            if (loading) {
                console.error("Already loading");
                return;
            }
            loading = true;
            const progressDialog = document.getElementById("progress-dialog");
            const progressIndicator = document.getElementById("progress-indicator");
            for (const idx of Array(NUM_FRAMES).keys()) {
                let url = value[idx].url
                let tmp_scene = new SPLAT.Scene();

                if (url.endsWith(".ply")) {
                    await SPLAT.PLYLoader.LoadAsync(url, tmp_scene, (progress) => {
                        // TODO: progress bar
                    });
                } else if (url.endsWith(".splat")) {
                    await SPLAT.Loader.LoadAsync(url, tmp_scene, (progress) => {
                        // TODO: progress bar
                    });
                } else {
                    throw new Error("Unsupported file type " + url);
                }

                frameIndexToObject[idx] = tmp_scene;

                // update progress bar
                if (progressIndicator != null) {
                    progressIndicator.value = Math.floor(((idx + 1) / NUM_FRAMES) * 100);
                }
            }
            loading = false;
            progressDialog.close();
            
            scene.addObject(frameIndexToObject[0]);
            animate();
        };

        function animate() {
			requestAnimationFrame(animate);
			controls.update();

            // change to the next frame after a short period
            if ((Date.now() - currTime > 100) && (Object.keys(frameIndexToObject).length == NUM_FRAMES)) {
                currTime = Date.now();
				currFrameIndex++;
				if (currFrameIndex >= NUM_FRAMES) currFrameIndex = 0;
            }
            renderer.render(frameIndexToObject[currFrameIndex], camera);

            // Attempt to improve the flickering issue with preloading using a buffer scene

			// if ((Date.now() - currTime > 200) && (Object.keys(frameIndexToObject).length == NUM_FRAMES)) {
            //     currTime = Date.now();
            //     let tmp_scene = new SPLAT.Scene();
            //     tmp_scene.addObject(frameIndexToObject[currFrameIndex]);
			// 	currFrameIndex++;
			// 	if (currFrameIndex >= NUM_FRAMES) currFrameIndex = 0;

            //     renderer.render(tmp_scene, camera);
            //     scene = tmp_scene;
            // } else {
            //     renderer.render(scene, camera);
            // }       
		}

        load();
    }

    onMount(() => {
        if (value != null) {
            reset_scene();
        }
        mounted = true;
    });

    $: canvas && mounted;


</script>

<BlockLabel {show_label} Icon={File} label={label || i18n("4DGS_model.splat")} />
    <div class="model4DGS">
        <div id="progress-container">
            <dialog open id="progress-dialog">
                <p>
                    <label for="progress-indicator">Loading scene...</label>
                </p>
                <progress max="100" id="progress-indicator"></progress>
            </dialog>
        </div>

        <canvas bind:this={canvas} />
    </div>

<style>
    .model4DGS {
        display: flex;
        position: relative;
        width: var(--size-full);
        height: var(--size-full);
    }
    canvas {
        width: var(--size-full);
        height: var(--size-full);
        object-fit: contain;
        overflow: hidden;
    }
    dialog {
        width: 100%;
        text-align: center;
        max-width: 20em;
        color: white;
        background-color: #000;
        border: none;
        position: relative;
        transform: translate(-50%, -50%);
    }
    #progress-container {
        position: absolute;
        top: 50%;
        left: 50%;
    }
    progress {
        width: 100%;
        height: 1em;
        border: none;
        background-color: #fff;
        color: #eee;
    }
    progress::-webkit-progress-bar {
        background-color: #333;
    }
    progress::-webkit-progress-value {
        background-color: #eee;
    }
    progress::-moz-progress-bar {
        background-color: #eee;
    }
</style>
