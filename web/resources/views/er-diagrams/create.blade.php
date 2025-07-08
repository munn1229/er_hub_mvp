<x-app-layout>
    <div class="bg-white rounded-2xl shadow-lg w-full max-w-md p-8">
        <h1 class="text-2xl font-semibold text-gray-800 mb-6 text-center">ER作成</h1>
        <form action="{{ route('er_diagrams.store') }}" method="POST" class="space-y-6">
            @csrf
            <div>
                <input type="hidden" name="project_id" value="{{ $projectId }}">
                <label for="name" class="block text-sm font-medium text-gray-700">
                    名称
                </label>
                <input 
                    type="text"
                    name="name"
                    id="name"
                    value="{{ old('name') }}"
                    class="mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-blue-500 focus:ring focus:ring-opacity-50"
                    placeholder="ER名"
                    required
                >
                @error('name')
                    <p class="mt-2 text-sm text-red-600">{{ $message }}</p>
                @enderror
            </div>
            <x-submit-button>作成</x-submit-button>
        </form>
    </div>
</x-app-layout>
