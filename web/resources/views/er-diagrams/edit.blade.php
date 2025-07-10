<x-app-layout>
    <div id="er-editor" class="flex flex-1 h-full" data-er-id="{{ $erDiagram['id'] }}" data-er='@json($er)'></div>
    
    @push('scripts')
        @vite('resources/js/editor.ts')
    @endpush
</x-app-layout>
