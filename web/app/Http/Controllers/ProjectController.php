<?php

namespace App\Http\Controllers;

use Illuminate\Http\Request;

class ProjectController extends Controller
{
    public function index(Request $request)
    {
        $projects = \ApiClient::get('projects');
        return view(
            'projects.index',
            [
                'projects' => $projects,
            ]
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
        $project = \ApiClient::post('projects', array_merge(
            $request->only(['name']),
            [
                'user_id' => auth()->user()->id,
            ]
        ));
        return redirect(route('projects.er_diagrams.index', $project['id']));
    }
}
