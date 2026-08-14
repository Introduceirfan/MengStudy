<?php

require_once __DIR__ . '/../vendor/autoload.php';

class Weather {
    public function __construct(private string $apiKey) {}

    public function getWeather(string $city): array 
    {
        $client = new \GuzzleHttp\Client();
        
        $response = $client->get('https://api.openweathermap.org/data/2.5/weather', [
            'query' => [
                'q'     => $city,
                'appid' => $this->apiKey,
                'units' => 'metric'
            ]
        ]);

        return json_decode($response->getBody(), true);
    }

    public function display(array $data): void
    {
        $city     = $data['name'];
        $country  = $data['sys']['country'];
        $temp     = $data['main']['temp'];
        $feels    = $data['main']['feels_like'];
        $desc     = $data['weather'][0]['description'];
        $humidity = $data['main']['humidity'];

        echo "============================\n";
        echo "  Weather in {$city}, {$country}\n";
        echo "============================\n";
        echo "  Temp     : {$temp}°C\n";
        echo "  Feels    : {$feels}°C\n";
        echo "  Condition: {$desc}\n";
        echo "  Humidity : {$humidity}%\n";
        echo "============================\n";
    }
}