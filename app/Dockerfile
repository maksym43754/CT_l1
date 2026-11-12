# Використовуємо зафіксовану версію slim-образу
FROM python:3.11-slim

# Створюємо непривілейованого користувача
RUN useradd -m appuser

# Встановлюємо робочу директорію
WORKDIR /app

# Спочатку копіюємо та встановлюємо залежності (окремий шар кешування)
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Копіюємо решту коду
COPY . .

# Змінюємо власника файлів на appuser
RUN chown -R appuser:appuser /app

# Перемикаємося на непривілейованого користувача
USER appuser

EXPOSE 8000

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]