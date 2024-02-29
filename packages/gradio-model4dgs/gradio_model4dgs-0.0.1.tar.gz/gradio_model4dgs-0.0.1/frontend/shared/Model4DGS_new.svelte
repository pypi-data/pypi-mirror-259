<script lang="ts">
    import type { FileData } from "@gradio/client";
    import { BlockLabel } from "@gradio/atoms";
    import { File } from "@gradio/icons";
    import { onMount } from "svelte";
    import * as GaussianSplats3D from "@mkkellogg/gaussian-splats-3d";
    import * as THREE from "three";
    import type { I18nFormatter } from "@gradio/utils";

    export let value: FileData[] | null;
    export let label = "";
    export let show_label: boolean;
    export let i18n: I18nFormatter;

    let currFrameIndex = 0;
    let NUM_FRAMES = 1;

    var sceneOptions: Array<object> = []
    const visible_scale = new THREE.Vector3(1.25, 1.25, 1.25);
    const invisible_scale = new THREE.Vector3(0.01, 0.01, 0.01);

    onMount(() => {
        if (value != null) {
            const viewerContainer = document.querySelector('.model4DGS');
            const viewer = new GaussianSplats3D.Viewer({
                cameraUp: [0, 1, 0],
                initialCameraPosition: [0, 0, 4],
                initialCameraLookAt: [0, 0, -1],
                dynamicScene: true,
                sharedMemoryForWorkers: false,
                rootElement: viewerContainer
            });

            console.log("value: ",value);

            NUM_FRAMES = value.length;

            for (let i = 0; i < value.length; i++) {
                let opt = {
                    // path: "@fs/data/home/cunjun/jwren/gradio-splatting/assets/tiger_4d_model_" + idx + ".ply",
                    path: "@fs" + value[i].path,
                    scale: [invisible_scale, invisible_scale, invisible_scale]
                };
                sceneOptions.push(opt);
            }

            viewer
                .addSplatScenes(sceneOptions,true,)
                .then(() => {
                    viewer.start();

                    let startTime = performance.now();
                    requestAnimationFrame(update);
                    function update() {
                        requestAnimationFrame(update);
                        const timeDelta = performance.now() - startTime;

                        if (timeDelta > 100) {
                            const prevSplatScene = viewer.getSplatScene(currFrameIndex);
                            prevSplatScene.scale.copy(invisible_scale);

                            startTime = performance.now();
                            currFrameIndex++;
                            if (currFrameIndex >= NUM_FRAMES) currFrameIndex = 0;

                            const curSplatScene = viewer.getSplatScene(currFrameIndex);
                            curSplatScene.scale.copy(visible_scale);
                        }
                    }
                });
        }
    });
</script>

<BlockLabel {show_label} Icon={File} label={label || i18n("4DGS_model.splat")} />
<div class="model4DGS">
</div>

<style>
    .model4DGS {
        display: flex;
        position: relative;
        width: var(--size-full);
        height: var(--size-full);
        min-height: 250px;
    }
    canvas {
        width: var(--size-full);
        height: var(--size-full);
        object-fit: contain;
        overflow: hidden;
    }
</style>

