<?php
    require './config.php';
    require 'vendor/autoload.php';
    require 'class-projects.php';

    function error(string $msg) {
        error_log($msg);
        http_response_code(500);
        json_response(["error" => $msg]);
    }

    function json_response(array $res) {
        // Enable CORS
        header('Access-Control-Allow-Origin: *');
        echo json_encode($res);
        die();
    }

    if (empty($_GET["action"])) {
        error("No action");
    }

    $action = $_GET["action"];

    if ($action == "get-projects") {
        $projects = new Projects();

        try {
            $items = $projects->getAll();
        } catch (Throwable $e) {
            error($e->getMessage());
        }

        json_response($items);
    } else {
        error("Invalid action");
    }