<x-app-layout>
    <div id="er-editor" class="flex flex-1 h-full"></div>
    
    @push('scripts')
        @vite('resources/js/editor.ts')
    @endpush
</x-app-layout>
