<?php
use GuzzleHttp\Client;
use League\Csv\Reader;

class Projects {
    function __construct() {

    }

    public function getAllAsArray():array {
        $csv = $this->getDriveCsvData();
        return $this->csvAsJson($csv);
    }

    public function getAllAsCsv():string {
        return $this->getDriveCsvData();
    }

    private function csvAsJson(string $csv):array {
        // Use the League CSV reader and export to JSON
        $reader = Reader::createFromString($csv);
        $reader->setHeaderOffset(0);
        $reader->getHeader();

        // Probably could be simpler than this
        $records = [];

        foreach ($reader->getRecords() as $record) {
            $records[] = $record;
        }

        return $records;
    }

    private function getDriveCsvData() {
        $drive = Config::DRIVE_ENDPOINT;
        $gid = Config::GID_ID;
        $url = "$drive/export?format=csv&gid=$gid";

        error_log("Getting $url");

        $client = new Client();
        $req = $client->get($url);

        if ($req->getStatusCode() !== 200) {
            throw new Exception("Something went wrong");
        }

        $body = (string) $req->getBody();

        return $body;
    }
}