<?php

use App\Http\Controllers\ErDiagramController;
use App\Http\Controllers\ProfileController;
use App\Http\Controllers\ProjectController;
use Illuminate\Support\Facades\Route;

/*
|--------------------------------------------------------------------------
| Web Routes
|--------------------------------------------------------------------------
|
| Here is where you can register web routes for your application. These
| routes are loaded by the RouteServiceProvider and all of them will
| be assigned to the "web" middleware group. Make something great!
|
*/

Route::get('/', function () {
    return view('welcome');
});

Route::get('/dashboard', function () {
    return view('dashboard');
})->middleware(['auth', 'verified'])->name('dashboard');

Route::middleware('auth')->group(function () {
    Route::get('/profile', [ProfileController::class, 'edit'])->name('profile.edit');
    Route::patch('/profile', [ProfileController::class, 'update'])->name('profile.update');
    Route::delete('/profile', [ProfileController::class, 'destroy'])->name('profile.destroy');

    Route::prefix('/projects')->as('projects.')->group(function() {
        Route::resource('/', ProjectController::class)->only('create');
        Route::resource('{projectId}/er_diagrams', ErDiagramController::class)->only('create');
    });
});

Route::prefix('/projects')->as('projects.')->group(function() {
    Route::resource('/', ProjectController::class)->only('index');
    Route::resource('{projectId}/er_diagrams', ErDiagramController::class)->only('index', 'show', 'edit');
});

require __DIR__.'/auth.php';
