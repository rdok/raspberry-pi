<?php

declare(strict_types=1);

namespace App\Db;

use App\Temperature\ProvidesTemperature;

final class DbClient implements ProvidesDbClient
{
    public function storeTemperature(ProvidesTemperature $temperature): array
    {
        // TODO: Implement storeTemperature() method.
    }
}