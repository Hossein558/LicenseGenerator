<?php
function desktopcenter_scripts() {
    wp_enqueue_style('desktopcenter-style', get_stylesheet_uri());
    // Load custom font (Vazirmatn or similar from CDN or local)
    wp_enqueue_style('vazirmatn-font', 'https://cdn.jsdelivr.net/gh/rastikerdar/vazirmatn@v33.0.3/misc/Farsi-Digits/font-face.css');
}
add_action('wp_enqueue_scripts', 'desktopcenter_scripts');

function desktopcenter_setup() {
    add_theme_support('title-tag');
    add_theme_support('post-thumbnails');
    add_theme_support('woocommerce');
}
add_action('after_setup_theme', 'desktopcenter_setup');
