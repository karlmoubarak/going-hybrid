<?php
use GuzzleHttp\Client;

class Projects {
    function __construct() {

    }

    public function getAll() {
        $data = $this->getDriveData();
        return $data;
    }

    private function getDriveData() {
        $drive = Config::DRIVE_ENDPOINT;
        $gid = Config::GID_ID;
        $url = "$drive/export?format=csv&gid=$gid";
        $client = new Client();
        $req = $client->get($url);

        if ($req->getStatusCode() !== 200) {
            throw new Exception("Something went wrong");
        }

        return $req->getBody();
    }
}