import sqlite3

# Veritabanına bağlan
conn = sqlite3.connect('database.db')
print("Connected to database successfully")

# Soruları ekle
questions = [
    # Python'da AI Geliştirme
    {
        "question": "Yapay zeka geliştirme sürecinde hangi adım ilk sırada yer alır?",
        "options": "Model eğitimi, Veri toplama, Model doğrulama, Sonuç analizi",
        "correct_answer": "Veri toplama"
    },
    {
        "question": "Bir yapay zeka modelini optimize etmek için kullanılan yöntem nedir?",
        "options": "Backpropagation, Veri temizleme, Özellik mühendisliği, Overfitting",
        "correct_answer": "Backpropagation"
    },
    {
        "question": "Python'da yapay zeka projelerinde hangi kütüphane sıkça kullanılır?",
        "options": "NumPy, TensorFlow, Pandas, Flask",
        "correct_answer": "TensorFlow"
    },
    {
        "question": "Bir modelin performansını artırmak için kullanılan yöntemlerden biri nedir?",
        "options": "Veriyi küçültme, Daha büyük bir model seçme, Eğitim verisini artırma, Modeli daha az eğitme",
        "correct_answer": "Eğitim verisini artırma"
    },
    # Bilgisayar Görüşü
    {
        "question": "Bilgisayar görüşünde kullanılan temel veri türü nedir?",
        "options": "Metin dosyaları, Görüntüler, Ses dosyaları, Grafikler",
        "correct_answer": "Görüntüler"
    },
    {
        "question": "Hangi Python kütüphanesi bilgisayar görüşü projelerinde sıkça kullanılır?",
        "options": "OpenCV, Matplotlib, Flask, Seaborn",
        "correct_answer": "OpenCV"
    },
    {
        "question": "Bir görüntüdeki nesneleri algılamak için kullanılan yöntem nedir?",
        "options": "KNN algoritması, Evrişimsel Sinir Ağı (CNN), LSTM algoritması, Karar ağacı",
        "correct_answer": "Evrişimsel Sinir Ağı (CNN)"
    },
    {
        "question": "Bir görüntüyü gri tonlamaya dönüştürmek için kullanılan OpenCV fonksiyonu nedir?",
        "options": "cv2.resize(), cv2.cvtColor(), cv2.rotate(), cv2.flip()",
        "correct_answer": "cv2.cvtColor()"
    },
    # NLP (Nöro-Dilbilim)
    {
        "question": "Hangi Python kütüphanesi doğal dil işleme için yaygın olarak kullanılır?",
        "options": "nltk, NumPy, Pandas, OpenCV",
        "correct_answer": "nltk"
    },
    {
        "question": "Metinleri küçük harfe çevirmek hangi işlemin bir parçasıdır?",
        "options": "Stopwords kaldırma, Lemmalaştırma, Tokenization, Ön işleme",
        "correct_answer": "Ön işleme"
    },
    {
        "question": "Bir metindeki anlamlı kelimeleri ayıklamak için kullanılan yöntem nedir?",
        "options": "Stopwords kaldırma, PCA analizi, Görüntü işleme, Evrişimsel ağ",
        "correct_answer": "Stopwords kaldırma"
    },
    {
        "question": "TF-IDF yöntemi hangi amaçla kullanılır?",
        "options": "Bir metindeki kelimelerin önemini belirlemek, Metinleri görselleştirmek, Veri kümesini bölmek, Görüntü verilerini dönüştürmek",
        "correct_answer": "Bir metindeki kelimelerin önemini belirlemek"
    },
    # Python Uygulamalarında AI Modelleri Uygulama
    {
        "question": "Bir AI modeli Flask kullanarak nasıl dağıtılır?",
        "options": "Modeli bir sunucuya yüklemek, Bir API oluşturmak, Modeli JSON formatında döndürmek, Hepsi",
        "correct_answer": "Hepsi"
    },
    {
        "question": "Bir AI modelini kaydetmek için hangi Python kütüphanesi kullanılır?",
        "options": "joblib, NumPy, Pandas, Seaborn",
        "correct_answer": "joblib"
    },
    {
        "question": "Model tahminlerini test etmek için hangi yöntem kullanılır?",
        "options": "Eğitim verisi kullanımı, Test verisi kullanımı, Görüntü işleme, Lemmalaştırma",
        "correct_answer": "Test verisi kullanımı"
    },
    {
        "question": "Flask’te bir modeli entegre etmek için ilk adım nedir?",
        "options": "Modeli yüklemek, Bir API oluşturmak, Modeli eğitmek, Modeli test etmek",
        "correct_answer": "Modeli yüklemek"
    }
]


# Soruları veritabanına ekle
for q in questions:
    conn.execute(
        "INSERT INTO questions (questions, options, correct_answer) VALUES (?, ?, ?)",
        (q["question"], q["options"], q["correct_answer"])
    )
    print(f"Added question: {q['question']}")

conn.commit()
conn.close()
print("Questions added successfully!")
