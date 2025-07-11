<x-app-layout>
    <div>
        <div class="flex justify-between mb-4">
            <div>
                <h1 class="text-2xl font-bold">プロジェクト一覧</h1>
            </div>
            @auth
                <x-link-button :to="route('projects.create')">新規作成</x-link-button>
            @endauth
        </div>

        <div class="overflow-x-auto">
            <table class="min-w-full bg-white border border-gray-200">
                <thead>
                    <tr class="bg-gray-100 text-left">
                        <th class="px-4 py-2 border-b">名称</th>
                    </tr>
                </thead>
                <tbody>
                    @forelse ($projects as $project)
                        <tr class="hover:bg-gray-50">
                            <td class="px-4 py-2 border-b">
                                <a href="{{ route('projects.er_diagrams.index', $project['id']) }}" class="text-blue-600 hover:underline">
                                    {{ $project['name'] }}
                                </a>
                            </td>
                        </tr>
                    @empty
                        <tr>
                            <td class="px-4 py-2 border-b text-gray-500">プロジェクトが存在しません</td>
                        </tr>
                    @endforelse
                </tbody>
            </table>
        </div>
    </div>
</x-app-layout>
