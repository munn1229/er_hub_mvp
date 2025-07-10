import { createApp } from 'vue'
import ErEditor from './components/ErEditor.vue'

const editor = document.getElementById('er-editor')
if (!editor) throw new Error('#er-editor not found')

const erDiagramId = Number(editor.dataset.erId)
const er = JSON.parse(editor.dataset.er || '{}')

createApp(ErEditor, {erDiagramId, er}).mount(editor)
