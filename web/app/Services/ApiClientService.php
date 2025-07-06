<?php

namespace App\Services;

use GuzzleHttp\Client;
use GuzzleHttp\Exception\GuzzleException;

class ApiClientService
{
    protected Client $http;

    public function __construct()
    {
        $this->http = new Client([
            'base_uri' => config('api_client.base_url'),
            'timeout'  => 5.0,
            'headers'  => [
                'Accept'        => 'application/json',
                'Authorization' => 'Bearer ' . config('api_client.token'),
            ],
        ]);
    }

    private function apiCall(string $url, string $method, array $options = []): array
    {
        try {
            $opts = array_merge_recursive(
                ['headers' => []],
                $options
            );

            $response = $this->http->request($method, $url, $opts);

            return json_decode($response->getBody()->getContents(), true);
        } catch (GuzzleException $e) {
            throw $e;
        }
    }

    public function get(string $url, array $query = []): array
    {
        return $this->apiCall($url, 'GET', ['query' => $query]);
    }

    public function post(string $url, array $data = []): array
    {
        return $this->apiCall($url, 'POST', ['json' => $data]);
    }

    public function put(string $url, array $data = []): array
    {
        return $this->apiCall($url, 'PUT', ['json' => $data]);
    }

    public function delete(string $url, array $query = []): array
    {
        return $this->apiCall($url, 'DELETE', ['query' => $query]);
    }
}
