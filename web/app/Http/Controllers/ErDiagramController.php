<?php

namespace App\Http\Controllers;

use Illuminate\Http\Request;

class ErDiagramController extends Controller
{
    public function index($projectId, Request $request)
    {
        $erDiagrams = \ApiClient::get('er_diagrams', [
            'project_id' => $projectId,
        ]);
        return view(
            'er-diagrams.index',
            [
                'projectId'  => $projectId,
                'erDiagrams' => $erDiagrams,
            ]
        );
    }

    public function show($projectId, $er_diagram)
    {
        return $er_diagram;
    }

    public function create($projectId)
    {
        return view(
            'er-diagrams.create',
            [
                'projectId' => $projectId,
            ]
        );
    }

    public function store(Request $request)
    {
        $erDiagram = \ApiClient::post('er_diagrams', array_merge($request->only([
            'project_id',
            'name',
        ]), [
            'user_id' => auth()->user()->id,
        ]));
        return redirect(route('projects.er_diagrams.show', [
            'projectId'  => $request->project_id,
            'er_diagram' => $erDiagram['id']
        ]));
    }
}
