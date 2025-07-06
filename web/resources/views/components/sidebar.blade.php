@props([
    // メニュー項目の配列。ラベルとURLを指定
    'menu' => [
        ['label' => 'ダッシュボード', 'url' => route('dashboard')],
        ['label' => 'プロジェクト', 'url' => route('projects.index')],
    ],
])

<aside class="w-56 bg-white shadow h-full flex flex-col">
    <div class="px-6 py-4 border-b">
        <h1 class="text-xl font-bold">ERHub</h1>
    </div>

    <nav aria-label="サイドメニュー" class="flex-1 overflow-y-auto">
        <ul class="space-y-1">
            @foreach($menu as $item)
                {{-- 現在の URL と一致するリンクは強調表示 --}}
                @php $isActive = url()->current() === $item['url']; @endphp
                <li>
                    <a
                        href="{{ $item['url'] }}"
                        class="block px-4 py-2 hover:bg-gray-100 {{ $isActive ? 'bg-gray-100 font-semibold' : '' }}"
                        @if($isActive) aria-current="page" @endif
                    >
                        {{ $item['label'] }}
                    </a>
                </li>
            @endforeach
        </ul>
    </nav>

    {{-- フッター／その他のリンクがあれば --}}
    <div class="px-6 py-4 border-t text-sm text-gray-500">
        設定
    </div>
</aside>
