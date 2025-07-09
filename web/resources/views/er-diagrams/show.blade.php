<x-app-layout>
    <div>
        <div class="flex mb-4 items-center">
            <div>
                <h1 class="text-2xl font-bold">{{ $erDiagram['name'] }}</h1>
            </div>
            @auth
                <div class="ml-8">
                    <x-link-button :to="route('projects.er_diagrams.edit', ['projectId' => $projectId, 'er_diagram' => $erDiagram['id']])">編集</x-link-button>
                </div>
            @endauth
        </div>
    </div>
</x-app-layout>
