<?php

class StringHelper
{
    public static function capitalize(string $str): string
    {
        return ucfirst(strtolower($str));
    }

    public static function slugify(string $str): string
    {
        $str = strtolower(trim($str));
        $str = preg_replace('/[\s_]+/', '-', $str);
        $str = preg_replace('/[^\w-]+/', '', $str);
        $str = preg_replace('/--+/', '-', $str);
        return $str;
    }

    public static function truncate(string $str, int $maxLength = 100): string
    {
        if (mb_strlen($str) <= $maxLength) return $str;
        return rtrim(mb_substr($str, 0, $maxLength)) . '...';
    }

    public static function isEmail(string $email): bool
    {
        return filter_var($email, FILTER_VALIDATE_EMAIL) !== false;
    }

    public static function mask(string $str, int $start = 4, int $end = 4, string $char = '*'): string
    {
        $length = mb_strlen($str);
        $maskLength = max(0, $length - $start - $end);
        return mb_substr($str, 0, $start) . str_repeat($char, $maskLength) . mb_substr($str, -$end);
    }
}


class DateHelper
{
    public static function formatDate(string $date, string $format = 'd F Y'): string
    {
        return date($format, strtotime($date));
    }

    public static function daysBetween(string $dateA, string $dateB): int
    {
        $diff = abs(strtotime($dateB) - strtotime($dateA));
        return (int) floor($diff / 86400);
    }

    public static function isToday(string $date): bool
    {
        return date('Y-m-d', strtotime($date)) === date('Y-m-d');
    }

    public static function timeAgo(string $date): string
    {
        $seconds = time() - strtotime($date);

        $intervals = [
            ['label' => 'tahun',   'seconds' => 31536000],
            ['label' => 'bulan',   'seconds' => 2592000],
            ['label' => 'hari',    'seconds' => 86400],
            ['label' => 'jam',     'seconds' => 3600],
            ['label' => 'menit',   'seconds' => 60],
            ['label' => 'detik',   'seconds' => 1],
        ];

        foreach ($intervals as $interval) {
            $count = (int) floor($seconds / $interval['seconds']);
            if ($count >= 1) {
                return "{$count} {$interval['label']} yang lalu";
            }
        }

        return 'baru saja';
    }

    public static function isLeapYear(int $year): bool
    {
        return ($year % 4 === 0 && $year % 100 !== 0) || ($year % 400 === 0);
    }
}


class ArrayHelper
{
    public static function chunk(array $arr, int $size): array
    {
        return array_chunk($arr, $size);
    }

    public static function groupBy(array $arr, string $key): array
    {
        $result = [];
        foreach ($arr as $item) {
            $group = is_array($item) ? $item[$key] : $item->$key;
            $result[$group][] = $item;
        }
        return $result;
    }

    public static function unique(array $arr): array
    {
        return array_values(array_unique($arr));
    }

    public static function flatten(array $arr): array
    {
        return array_merge(...array_map(fn($v) => (array) $v, $arr));
    }

    public static function randomItem(array $arr): mixed
    {
        return $arr[array_rand($arr)];
    }

    public static function pluck(array $arr, string $key): array
    {
        return array_column($arr, $key);
    }
}
