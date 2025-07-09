<template>
    <div class="flex h-full w-full">
        <aside class="w-64 bg-gray-100 border-r p-4 flex flex-col">
            <h2 class="text-lg font-semibold mb-4">Palette</h2>
            <div class="space-y-2">
                <button
                    class="w-full bg-white border rounded py-2 text-left hover:bg-gray-200 disabled:opacity-50"
                    disabled
                >
                    + Table
                </button>
            </div>
            <div class="mt-auto">
                <button
                    id="commit-btn"
                    class="w-full bg-blue-600 text-white py-2 rounded hover:bg-blue-700"
                >
                    Commit
                </button>
            </div>
        </aside>

        <div
            ref="container"
            class="flex-1 bg-white relative overflow-hidden cursor-grab"
            @wheel.prevent="onWheel"
            @mousedown="onPanStart"
            @mousemove="onPanMove"
            @mouseup="onPanEnd"
            @mouseleave="onPanEnd"
        >
            <div
                class="absolute top-0 left-0 grid-background"
                :style="canvasStyle">
                <div class="w-full h-full flex items-center justify-center text-gray-400">
                    Canvas Area (coming soon)
                </div>
            </div>
        </div>
    </div>
</template>

<script lang="ts" setup>
    import { ref, reactive, computed } from 'vue'

    const container = ref<HTMLElement | null>(null)

    const state =  reactive({
        scale: 1,
        offsetX: 0,
        offsetY: 0,
        isPanning: false,
        startX: 0,
        startY: 0,
    })

    function onWheel(e: WheelEvent) {
        if (!container.value) return
        const delta = -e.deltaY * 0.001
        const newScale = Math.min(Math.max(state.scale + delta, 0.1), 4)

        const rect = container.value.getBoundingClientRect()
        const cx = e.clientX - rect.left
        const cy = e.clientY - rect.top
        const xRel = (cx - state.offsetX) / state.scale
        const yRel = (cy - state.offsetY) / state.scale

        state.scale = newScale
        state.offsetX = cx - xRel * newScale
        state.offsetY = cy - yRel * newScale
    }

    function onPanStart(e: MouseEvent) {
        state.isPanning = true
        state.startX = e.clientX - state.offsetX
        state.startY = e.clientY - state.offsetY
        if (container.value) {
            container.value.style.cursor = 'grabbing'
        }
    }

    function onPanMove(e: MouseEvent) {
        if (!state.isPanning) return
        state.offsetX = e.clientX - state.startX
        state.offsetY = e.clientY - state.startY
    }

    function onPanEnd() {
        state.isPanning = false
        if (container.value) {
            container.value.style.cursor = 'grab'
        }
    }

    const canvasStyle = computed(() => ({
        transform: `translate(${state.offsetX}px, ${state.offsetY}px) scale(${state.scale})`,
        transformOrigin: '0 0',
        width: '100%',
        height: '100%',
    }))
</script>

<style scoped>
.cursor-grab {
    cursor: grab;
}

.grid-background {
    background-image:
        linear-gradient(to right, #ddd 1px, transparent 1px),
        linear-gradient(to bottom, #ddd 1px, transparent 1px),
        linear-gradient(to right, #aaa 2px, transparent 2px),
        linear-gradient(to bottom, #aaa 2px, transparent 2px);
    background-size:
        20px 20px,
        20px 20px,
        100px 100px,
        100px 100px;
    background-position: 0 0, 0 0, 0 0, 0 0;
}
</style>
