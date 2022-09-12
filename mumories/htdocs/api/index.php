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
        header("Content-Type: application/json");
        response(json_encode($res));
    }

    function response(string $res) {
        // Enable CORS
        header('Access-Control-Allow-Origin: *');
        echo $res;
        die();
    }

    if (empty($_GET["action"])) {
        error("No action");
    }

    $action = $_GET["action"];

    if ($action == "get-projects") {
        $projects = new Projects();
        $format = isset($_GET["format"]) ? $_GET["format"] : "json";

        try {
            if ($format == "csv") {
                response( $projects->getAllAsCsv() );
            } else if ($format == "json") {
                json_response( $projects->getAllAsArray() );
            } else {
                error("Invalid format");
            }
        } catch (Throwable $e) {
            error($e->getMessage());
        }

        json_response(["items" => $items]);
    } else {
        error("Invalid action");
    }