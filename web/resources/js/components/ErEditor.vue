<template>
    <div class="flex h-full w-full">
        <aside class="w-64 bg-gray-100 border-r p-4 flex flex-col">
            <h2 class="text-lg font-semibold mb-4">Palette</h2>
            <div class="space-y-2">
                <button
                    class="w-full bg-white border rounded py-2 text-left hover:bg-gray-200 disabled:opacity-50"
                    @click="addTable"
                >
                    + Table
                </button>
            </div>
            <div class="mt-auto">
                <button
                    id="commit-btn"
                    class="w-full bg-blue-600 text-white py-2 rounded hover:bg-blue-700"
                    :disabled="isSaving"
                    @click="save"
                >
                    {{ isSaving ? 'Saving...' : 'Commit' }}
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
                <div
                    v-for="table in tables"
                    :key="table.id"
                    class="absolute bg-white border shadow w-32"
                    :style="{
                        top: `${table.y}px`,
                        left: `${table.x}px`
                    }"
                    @mousedown.stop="startDrag(table, $event)"
                >
                    <div class="px-2 py-1 border-b cursor-move">
                        <input
                            v-model="table.name"
                            type="text"
                            class="w-full text-sm font-semibold outline-none"
                            placeholder="Table name"
                        />
                    </div>
                    <div class="p-2 text-xs text-gray-500">Columns / Indexes...</div>
                </div>
            </div>
        </div>
    </div>
</template>

<script lang="ts" setup>
    import { ref, reactive, computed, onBeforeUnmount } from 'vue'
    import axios from 'axios'

    const isSaving = ref(false)

    const container = ref<HTMLElement | null>(null)

    const state =  reactive({
        scale: 1,
        offsetX: 0,
        offsetY: 0,
        isPanning: false,
        startX: 0,
        startY: 0,
    })

    interface Table {
        id: number
        name: string
        x: number
        y: number
    }

    interface ErPayload {
        tables?: Table[]
    }

    interface Props { 
        erDiagramId: number
        er: ErPayload
    }
    const props = defineProps<Props>()

    const tables = reactive<Table[]>(
        props.er.tables ? [...props.er.tables] : []
    )

    const dragState = reactive({
        tableId: null as number | null,
        startCanvasX: 0,
        startCanvasY: 0,
        x: 0,
        y: 0,
    })

    let nextTableId = tables.length + 1
    function addTable() {
        tables.push({
            id: nextTableId++,
            name: '',
            x: (container.value?.clientWidth ?? 0) / 2 - 64,
            y: (container.value?.clientHeight ?? 0) / 2 - 24,
        })
    }

    async function save() {
        if (isSaving.value) return
        isSaving.value = true
        try {
            const payload = {
                er_body: JSON.stringify({ tables }),
            }
            const res = await axios.patch(
                `/api/er_diagrams/${props.erDiagramId}`,
                payload
            )
            if (!res.data.success) {
                throw new Error(res.data.message || 'Save failed')
            }
            alert('Saved')
        } catch (e: any) {
            console.error(e)
            alert('Error: ' + (e.message || 'Unknown'))
        } finally {
            isSaving.value = false
        }
    }

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

    function startDrag(table: Table, e: MouseEvent) {
        const rect = container.value!.getBoundingClientRect()
        const canvasX = (e.clientX - rect.left - state.offsetX) / state.scale
        const canvasY = (e.clientY - rect.top - state.offsetY) / state.scale

        dragState.tableId = table.id
        dragState.startCanvasX = canvasX
        dragState.startCanvasY = canvasY
        dragState.x = table.x
        dragState.y = table.y

        document.addEventListener('mousemove', onTableDrag)
        document.addEventListener('mouseup', onTableDrop)
    }

    function onTableDrag(e: MouseEvent) {
        if (dragState.tableId === null) return
        const rect = container.value.getBoundingClientRect()
        const canvasX = (e.clientX - rect.left - state.offsetX) / state.scale
        const canvasY = (e.clientY - rect.top - state.offsetY) / state.scale
        const dx = canvasX - dragState.startCanvasX
        const dy = canvasY - dragState.startCanvasY

        const table = tables.find(t => t.id === dragState.tableId)
        if (table) {
            table.x = dragState.x + dx
            table.y = dragState.y + dy
        }
    }

    function onTableDrop() {
        document.removeEventListener('mousemove', onTableDrag)
        document.removeEventListener('mouseup', onTableDrop)
        dragState.tableId = null
    }

    onBeforeUnmount(() => {
        document.removeEventListener('mousemove', onTableDrag)
        document.removeEventListener('mouseup', onTableDrop)
    })

    const canvasStyle = computed(() => ({
        transform: `translate(${state.offsetX}px, ${state.offsetY}px) scale(${state.scale})`,
        transformOrigin: '0 0',
        width: '100%',
        height: '100%',
        backgroundSize: `${20*state.scale}px ${20*state.scale}px, ${20*state.scale}px ${20*state.scale}px, ${100*state.scale}px ${100*state.scale}px, ${100*state.scale}px ${100*state.scale}px`,
    }))
</script>

<style scoped>
.cursor-grab {
    cursor: grab;
}
.cursor-move {
    cursor: move;
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
