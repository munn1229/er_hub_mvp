<?php

namespace App\View\Components;

use Illuminate\View\Component;
use Illuminate\View\View;
use Illuminate\Support\Facades\Route;
use Illuminate\Support\Facades\File;

class ViteJs extends Component
{
    private const BASE_FILE = 'resources/ts/app.ts';
    private const PAGES_PATH = 'ts/pages/';

    public function __construct(
        public array $ts = [self::BASE_FILE],
    )
    {}

    /**
     * Get the view / contents that represents the component.
     */
    public function render(): View
    {
        $tsRouteFileName = str(Route::currentRouteName())->replace('.', '/')->value().'.ts';

        if (File::exists(resource_path($tsFileName = self::PAGES_PATH.$tsRouteFileName))) {
            $this->ts = array_merge($this->ts, ['resources/'.$tsFileName]);
        }

        return view('components.vite-js');
    }
}
