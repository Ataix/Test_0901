from django.core.cache import cache
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import WeatherSerializer
from .utils import get_weather


class WeatherAPIView(APIView):
    """
    Api that gets weather information from Get request. Using get_weather func
    sends request to OpenWeather, transforms response to dict. Caches data.
    """
    def get(self, request):
        serializer = WeatherSerializer(data=request.GET)
        serializer.is_valid()

        city = serializer.validated_data['city']

        weather_data = get_weather(city)

        if cache_data := cache.get(f"{city}"):
            return Response(weather_data)

        cache.set(f"{city}", weather_data, timeout=60 * 30) # Keeping cache for 30 min

        return Response(weather_data)
