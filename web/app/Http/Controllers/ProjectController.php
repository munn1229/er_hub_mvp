<?php

namespace App\Http\Controllers;

use Illuminate\Http\Request;

class ProjectController extends Controller
{
    public function index(Request $request)
    {
        return view(
            'projects.index'
        );
    }

    public function create()
    {
        return view(
            'projects.create'
        );
    }

    public function store(Request $request)
    {
        $project = \ApiClient::post('projects', $request->only(['name']));
        return redirect(route('projects.er_diagrams.index', $project['id']));
    }
}
