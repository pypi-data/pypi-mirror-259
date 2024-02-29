<script context="module" lang="ts">
    export { default as BaseModel4DGS } from "./shared/Model4DGS_new.svelte";
    export { default as BaseExample } from "./Example.svelte";
</script>

<script lang="ts">
    import { normalise_file, type FileData } from "@gradio/client";
    import Model4DGS from "./shared/Model4DGS_new.svelte";
    import { BlockLabel, Block, Empty, UploadText } from "@gradio/atoms";
    import { File } from "@gradio/icons";

    import { StatusTracker } from "@gradio/statustracker";
    import type { LoadingStatus } from "@gradio/statustracker";
    import type { Gradio } from "@gradio/utils";

    export let elem_id = "";
    export let elem_classes: string[] = [];
    export let visible = true;
    export let value: null | FileData[] = null;
    export let root: string;
    export let proxy_url: null | string;
    export let loading_status: LoadingStatus;
    export let label: string;
    export let show_label: boolean;
    export let container = true;
    export let scale: number | null = null;
    export let min_width: number | undefined = undefined;
    export let gradio: Gradio;
    export let height: number | undefined = undefined;

    let _value: null | FileData[];

    $: if (value !== null && value !== undefined) {
        _value = value.map(item => normalise_file(item, root, proxy_url));
    }

    let dragging = false;
</script>

<Block
    {visible}
    variant={value === null ? "dashed" : "solid"}
    border_mode={dragging ? "focus" : "base"}
    padding={false}
    {elem_id}
    {elem_classes}
    {container}
    {scale}
    {min_width}
    {height}
>
    <StatusTracker autoscroll={gradio.autoscroll} i18n={gradio.i18n} {...loading_status} />

    {#if value}
        <BlockLabel {show_label} Icon={File} label={label || "Splat"} />
        <Model4DGS
            value={_value}
            i18n={gradio.i18n}
            {label}
            {show_label}
        />
    {:else}
        <BlockLabel {show_label} Icon={File} label={label || "Splat"} />

        <Empty unpadded_box={true} size="large"><File /></Empty>
    {/if}
</Block>
