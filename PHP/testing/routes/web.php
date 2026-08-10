<?php

use Illuminate\Support\Facades\Route;

Route::get('/hello', function () {
    return view('hello', ['name' => 'Irfan']);
});
