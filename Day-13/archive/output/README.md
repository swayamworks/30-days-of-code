# Weather and Air Pollution for the 3 Biggest Cities per Country

This dataset contains current weather and current air pollution measurements for the 3 biggest cities per country, selected by GeoNames city population.

## Sources
- OpenWeather Current Weather API
- OpenWeather Air Pollution API
- GeoNames cities15000 dump
- GeoNames countryInfo

## Collection settings
- Units: metric
- Language: en
- Top cities per country: 3
- Minimum city population in source selection: 15000
- Generated at: 2026-04-24T07:07:49.156595+00:00

## Main target columns
- `aqi`
- `pm2_5`
- `pm10`

## Example ML tasks
- multiclass classification: predict `aqi`
- regression: predict `pm2_5`
- regression: predict `pm10`
