# Soil Nutrition Control System API

This API predicts the required fertilizer level based on soil nutrient values.

## Fertilizer Levels

1. **Level 1**: N-(0-10), P-(0-10), K-(0-10) - Add N, P, K (all nutrients are low)
2. **Level 2**: N-(0-10), P-(20-50), K-(20-50) - Add N (P and K are sufficient)
3. **Level 3**: N-(0-100), P-(0-20), K-(0-110) - Add P (N and K are sufficient)
4. **Level 4**: N-(0-100), P-(0-120), K-(0-20) - Add K (N and P are sufficient)
5. **Level 5**: N-(0-10), P-(0-20), K-(0-110) - Add N and P (K is sufficient)
6. **Level 6**: N-(0-100), P-(0-20), K-(0-20) - Add P and K (N is sufficient)
7. **Level 7**: N-(0-20), P-(0-120), K-(0-20) - Add N and K (P is sufficient)
8. **Level 8**: N-(40-100), P-(40-120), K-(40-110) - Perfect condition (no fertilizer needed)

## API Endpoints

- `/`: API status and information
- `/predict`: POST request with JSON data containing N, P, K, and pH values

## Example Request

```json
{
  "n": 70,
  "p": 80,
  "k": 70,
  "ph": 6
}