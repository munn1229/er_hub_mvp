<?php

namespace App\Http\Controllers;

use Illuminate\Http\Request;

class ErDiagramController extends Controller
{
    public function index($projectId, Request $request)
    {
        return $projectId;
    }
}
