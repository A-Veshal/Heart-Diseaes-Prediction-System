from django.shortcuts import render, redirect
from .forms import HeartForm
from .models import PredictionHistory
import joblib
import os
import pandas as pd
import matplotlib.pyplot as plt
from io import BytesIO
from django.http import HttpResponse

# Load the trained model
model_path = os.path.join(os.path.dirname(__file__), 'heart_model.pkl')
model = joblib.load(model_path)

def predict_view(request):
    if request.method == 'POST':
        form = HeartForm(request.POST)
        if form.is_valid():
            data = list(form.cleaned_data.values())

            df = pd.DataFrame([data], columns=[
                "age", "sex", "cp", "trestbps", "chol", "fbs", "restecg",
                "thalach", "exang", "oldpeak", "slope", "ca", "thal"
            ])

            prediction = model.predict(df)[0]
            probability = model.predict_proba(df)[0][1]

            # Save prediction to DB
            PredictionHistory.objects.create(
                age=data[0], sex=data[1], cp=data[2], trestbps=data[3], chol=data[4],
                fbs=data[5], restecg=data[6], thalach=data[7], exang=data[8],
                oldpeak=data[9], slope=data[10], ca=data[11], thal=data[12],
                prediction=prediction, probability=probability
            )

            return redirect('result')  # Redirect to result page

    else:
        form = HeartForm()

    return render(request, 'predictor/predict.html', {'form': form})


def result_view(request):
    history = PredictionHistory.objects.all().order_by('-timestamp')[:5]
    latest = history[0] if history else None

    if latest:
        if latest.prediction == 1:
            result = f"⚠️ You are at HIGH risk of heart disease. (Confidence: {latest.probability * 100:.2f}%)"
        else:
            result = f"✅ You are NOT at risk of heart disease. (Confidence: {latest.probability * 100:.2f}%)"
    else:
        result = "No predictions yet."

    return render(request, 'predictor/result.html', {
        'result': result,
        'history': history
    })


def cholesterol_chart(request):
    history = PredictionHistory.objects.all().order_by('-timestamp')[:5]
    history = list(history)[::-1]  # Reverse for chronological order

    labels = [f"#{i+1}" for i in range(len(history))]
    cholesterol = [h.chol for h in history]
    thalach = [h.thalach for h in history]

    fig, ax = plt.subplots()
    ax.plot(labels, cholesterol, label='Cholesterol', marker='o')
    ax.plot(labels, thalach, label='Max Heart Rate', marker='s')
    ax.set_title("Cholesterol vs Max Heart Rate")
    ax.set_xlabel("Prediction")
    ax.set_ylabel("Value")
    ax.legend()
    ax.grid(True)

    buffer = BytesIO()
    plt.tight_layout()
    plt.savefig(buffer, format='png')
    plt.close(fig)
    buffer.seek(0)

    return HttpResponse(buffer.getvalue(), content_type='image/png')
