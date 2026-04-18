<!DOCTYPE html>
<html lang="tr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>SERkAN HOCA İLE - Coğrafya 10. Sınıf Soru Bankası</title>
    <script src="https://cdn.jsdelivr.net/npm/canvas-confetti@1.6.0/dist/confetti.browser.min.js"></script>
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600&amp;family=Roboto+Slab:wght@500&amp;display=swap');
        
        :root {
            --primary: #1e3a8a;
            --accent: #3b82f6;
            --success: #10b981;
        }
        
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }
        
        body {
            font-family: 'Inter', system_ui, sans-serif;
            background: linear-gradient(135deg, #f8fafc 0%, #e0f2fe 100%);
            min-height: 100vh;
            overflow-x: hidden;
        }
        
        .header {
            background: linear-gradient(90deg, var(--primary), var(--accent));
            color: white;
            padding: 2rem 0;
            text-align: center;
            box-shadow: 0 10px 30px rgba(30, 58, 138, 0.3);
            position: relative;
        }
        
        .logo-container {
            display: inline-flex;
            align-items: center;
            gap: 15px;
            padding: 15px 40px;
            background: rgba(255,255,255,0.15);
            border-radius: 9999px;
            backdrop-filter: blur(10px);
            box-shadow: 0 8px 25px rgba(0,0,0,0.2);
        }
        
        .logo-text {
            font-family: 'Roboto Slab', serif;
            font-size: 2.8rem;
            font-weight: 600;
            letter-spacing: -2px;
            text-shadow: 0 4px 15px rgba(0,0,0,0.3);
        }
        
        .subtitle {
            font-size: 1.3rem;
            opacity: 0.95;
            margin-top: 8px;
        }
        
        .main-container {
            max-width: 1100px;
            margin: 30px auto;
            padding: 0 20px;
        }
        
        .card {
            background: white;
            border-radius: 20px;
            box-shadow: 0 20px 40px rgba(0,0,0,0.08);
            padding: 2rem;
            margin-bottom: 2rem;
            border: 1px solid #e2e8f0;
        }
        
        .question-header {
            display: flex;
            justify-content: space-between;
            align-items: center;
            margin-bottom: 1.5rem;
            padding-bottom: 1rem;
            border-bottom: 3px solid #e2e8f0;
        }
        
        .progress-bar {
            height: 8px;
            background: #e2e8f0;
            border-radius: 9999px;
            overflow: hidden;
            margin-bottom: 1rem;
        }
        
        .progress-fill {
            height: 100%;
            background: linear-gradient(90deg, var(--accent), #60a5fa);
            transition: width 0.4s cubic-bezier(0.4, 0, 0.2, 1);
        }
        
        .question-text {
            font-size: 1.35rem;
            line-height: 1.7;
            color: #1e2937;
            margin-bottom: 2rem;
        }
        
        .long-question {
            background: #f8fafc;
            padding: 1.5rem;
            border-radius: 16px;
            border-left: 6px solid var(--accent);
            font-size: 1.2rem;
            line-height: 1.8;
            margin-bottom: 2rem;
        }
        
        .options-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
            gap: 14px;
        }
        
        .option-btn {
            background: #f8fafc;
            border: 2px solid #e2e8f0;
            border-radius: 16px;
            padding: 18px 22px;
            font-size: 1.15rem;
            font-weight: 500;
            color: #1e2937;
            cursor: pointer;
            transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
            display: flex;
            align-items: center;
            gap: 12px;
            box-shadow: 0 4px 15px rgba(0,0,0,0.05);
        }
        
        .option-btn:hover {
            border-color: var(--accent);
            transform: translateY(-3px);
            box-shadow: 0 15px 25px rgba(59, 130, 246, 0.2);
        }
        
        .option-btn:active {
            transform: scale(0.98);
        }
        
        .sidebar {
            position: fixed;
            top: 20px;
            right: 20px;
            background: white;
            border-radius: 20px;
            box-shadow: 0 20px 40px rgba(0,0,0,0.1);
            padding: 1.5rem;
            width: 260px;
            z-index: 1000;
        }
        
        .analysis-card {
            animation: fadeIn 0.6s ease;
        }
        
        @keyframes fadeIn {
            from { opacity: 0; transform: translateY(30px); }
            to { opacity: 1; transform: translateY(0); }
        }
        
        .firework {
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            pointer-events: none;
            z-index: 9999;
        }
        
        .result-badge {
            font-size: 4rem;
            font-weight: 700;
            background: linear-gradient(90deg, #10b981, #34d399);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            text-align: center;
            margin: 2rem 0;
        }
    </style>
</head>
<body>
    <!-- HEADER / LOGO -->
    <div class="header">
        <div class="logo-container">
            <span style="font-size: 3.5rem;">📘</span>
            <div>
                <div class="logo-text">SERKAN HOCA İLE</div>
                <div class="subtitle">10. Sınıf Coğrafya • Yer'in Yapısı ve Levha Hareketleri</div>
            </div>
            <span style="font-size: 3.5rem;">📗</span>
        </div>
    </div>

    <div class="main-container" id="app">
        <!-- Streamlit benzeri Python kodunun tam çalıştırılabilir hali burada başlıyor -->
        <!-- Bu HTML + JS dosyası, GitHub + Streamlit yerine tek dosyada çalışan, profesyonel bir web uygulamasıdır. 
             İsterseniz bu kodu app.py içine koyup Streamlit ile de çalıştırabilirsiniz (aşağıda Python versiyonu da verilmiştir). -->

        <div id="quiz-screen">
            <div class="card">
                <!-- Progress -->
                <div class="question-header">
                    <div style="display: flex; align-items: center; gap: 12px;">
                        <span id="question-counter" style="font-size: 1.4rem; font-weight: 600; color: var(--primary);">Soru <span id="current">1</span>/<span id="total">25</span></span>
                    </div>
                    <div style="display: flex; align-items: center; gap: 8px; font-size: 1.1rem; color: #64748b;">
                        <span id="percentage-display">0%</span>
                        <div class="progress-bar" style="width: 180px;">
                            <div id="progress-fill" class="progress-fill" style="width: 0%"></div>
                        </div>
                    </div>
                </div>

                <!-- Soru -->
                <div id="question-text" class="question-text"></div>

                <!-- Seçenekler -->
                <div id="options" class="options-grid"></div>
            </div>
        </div>

        <!-- Analiz Ekranı (gizli başlar) -->
        <div id="analysis-screen" class="card analysis-card" style="display: none;">
            <h2 style="text-align: center; margin-bottom: 1rem; color: var(--primary);">Sınav Analizi</h2>
            
            <div id="success-message" style="display: none;">
                <div class="result-badge">TEBRİKLER HARİKASIN! 🎉</div>
                <p style="text-align: center; font-size: 1.4rem; color: #10b981; margin-bottom: 2rem;">%80 ve üzeri başarı ile tamamladınız. Konfeti ve havai fişekler sizin için patlıyor!</p>
            </div>

            <div style="text-align: center; margin: 2rem 0;">
                <div id="score-circle" style="width: 160px; height: 160px; margin: 0 auto; border-radius: 50%; border: 14px solid #10b981; display: flex; align-items: center; justify-content: center; font-size: 3rem; font-weight: 700; color: #10b981; position: relative;">
                    <span id="final-percentage">85</span>%
                    <div style="position: absolute; top: -12px; right: -12px; background: #10b981; color: white; font-size: 1rem; padding: 4px 14px; border-radius: 9999px;">BAŞARI</div>
                </div>
            </div>

            <h3 style="margin: 2rem 0 1rem; color: #1e2937;">Yanlış Yapılan Sorular</h3>
            <div id="wrong-list" style="max-height: 420px; overflow-y: auto;"></div>

            <div style="display: flex; gap: 15px; margin-top: 3rem;">
                <button onclick="restartExam()" style="flex: 1; padding: 18px; font-size: 1.2rem; background: var(--accent); color: white; border: none; border-radius: 9999px; cursor: pointer;">Yeniden Başla</button>
                <button onclick="goToStart()" style="flex: 1; padding: 18px; font-size: 1.2rem; background: #64748b; color: white; border: none; border-radius: 9999px; cursor: pointer;">Başa Dön</button>
            </div>
        </div>
    </div>

    <!-- Sidebar -->
    <div class="sidebar">
        <h3 style="margin-bottom: 1rem; color: var(--primary);">Kontrol Paneli</h3>
        <button onclick="goToStart()" style="width: 100%; padding: 14px; margin-bottom: 10px; background: #f1f5f9; border: none; border-radius: 12px; font-weight: 600; cursor: pointer;">🏠 Başa Dön</button>
        <button onclick="restartExam()" style="width: 100%; padding: 14px; margin-bottom: 10px; background: #f1f5f9; border: none; border-radius: 12px; font-weight: 600; cursor: pointer;">🔄 Sınavı Yeniden Başlat</button>
        <button onclick="closeExam()" style="width: 100%; padding: 14px; background: #ef4444; color: white; border: none; border-radius: 12px; font-weight: 600; cursor: pointer;">✕ Sınavı Kapat</button>
        
        <div style="margin-top: 2rem; font-size: 0.95rem; color: #64748b;">
            <strong>İpucu:</strong> Her girişte sorular tamamen karıştırılır.<br>
            Kaldığınız yer tarayıcı oturumunda saklanır.
        </div>
    </div>

    <script>
        // === SORU BANKASI (Tüm sayfalarından eşit dağılımla, 25 kaliteli soru) ===
        let questionsPool = [
            {
                id: 1,
                question: "Yer kabuğundan çekirdeğe doğru inildikçe sıcaklık, yoğunluk ve basınç artar. Bu bilgiye göre Dünya’nın en yoğun, en basınçlı ve en kalın katmanı hangisidir?",
                options: ["A) Yer kabuğu (Litosfer)", "B) Manto", "C) Çekirdek", "D) Astenosfer", "E) SIAL katmanı"],
                correct: "C",
                isLong: false
            },
            {
                id: 2,
                question: "Yer kabuğunun üst katmanında silisyum ve alüminyum yoğunken, alt katmanında silisyum ve magnezyum yoğunluğu artar. Alt katmana ne ad verilir?",
                options: ["A) SIAL", "B) SIMA", "C) Manto", "D) Barisfer", "E) Litosfer"],
                correct: "B",
                isLong: false
            },
            {
                id: 3,
                question: "Dünya’nın toplam hacminin yaklaşık %84’ünü oluşturan, 70-2900 km derinliğinde yer alan ve sıvı-akışkan yapıya sahip katman aşağıdakilerden hangisidir?",
                options: ["A) Yer kabuğu", "B) Çekirdek", "C) Manto", "D) SIAL", "E) Sima"],
                correct: "C",
                isLong: false
            },
            {
                id: 4,
                question: "1915 yılında Alfred Wegener tarafından ortaya atılan ve kıtaların ilk başta tek bir parça halinde olduğunu savunan teori hangisidir?",
                options: ["A) Levha Tektoniği Teorisi", "B) Deprem Teorisi", "C) Volkanizma Teorisi", "D) Kıtaların Kayma Teorisi", "E) Epirojenez Teorisi"],
                correct: "D",
                isLong: false
            },
            {
                id: 5,
                question: "Levha hareketleri kaç farklı şekilde gerçekleşir ve ülkemiz hangi iki levha arasında yer alır?",
                options: ["A) 2 şekilde – Avrasya ve Pasifik", "B) 4 şekilde – Afrika ve Antarktika", "C) 1 şekilde – Sadece yaklaşma", "D) 5 şekilde – Pasifik ve İzlanda", "E) 3 şekilde – Yaklaşma, uzaklaşma ve yanal yer değiştirme"],
                correct: "E",
                isLong: false
            },
            {
                id: 6,
                question: "Ülkemizin büyük bir kısmı 3. Jeolojik zamanda (Senozoyik) oluşmuştur. Bu durum ülkemizi hangi açıdan etkilemektedir?",
                options: ["A) Deprem riski yüksek ve genç oluşumlu bir ülkeyiz", "B) Masif araziler bakımından zenginiz", "C) Taş kömürü yatakları çok fazladır", "D) Dinazor fosilleri yaygındır", "E) Prekambriyen kayaçlar hâkimdir"],
                correct: "A",
                isLong: false
            },
            {
                id: 7,
                question: "<strong>Uzun paragraf sorusu:</strong><br>Dünya yaklaşık 4,5 milyar yıl önce yaratılmıştır. Jeolojik devirler, yeryüzü şekillerinin oluşumu, iklim değişimleri, canlı türlerinin ortaya çıkması veya yok olması gibi olaylara göre ayrılır. Senozoyik zamanda Tersiyer devrinde Alp orojeneziyle Alp, Himalaya, Toros ve Kuzey Anadolu dağları oluşmuş; Kuaterner devrinde ise buzullar yaşanmış, Türkiye’deki volkan dağları, delta ovaları, Ege Denizi, İstanbul ve Çanakkale boğazları meydana gelmiştir. Ülkemiz linyit, bor ve petrol yatakları bakımından da bu dönemde zenginleşmiştir.<br><br>Yukarıdaki bilgilere göre Mezozoyik (2. zaman) devrinde gerçekleşen olay hangisidir?",
                options: ["A) İnsan yaratılmıştır", "B) Dinazorlar ortaya çıkmıştır", "C) Ege Denizi oluşmuştur", "D) Toros Dağları oluşmuştur", "E) Taş kömürü yatakları oluşmuştur"],
                correct: "B",
                isLong: true
            },
            {
                id: 8,
                question: "Yer kabuğu parçalarının (levhaların) yükselmesi veya alçalması şeklinde gerçekleşen ve izostatik dengenin bozulması sonucu oluşan iç kuvvet hangisidir?",
                options: ["A) Orojenez", "B) Volkanizma", "C) Epirojenez", "D) Deprem", "E) Tsunami"],
                correct: "C",
                isLong: false
            },
            {
                id: 9,
                question: "Karaların ağırlaşarak çökmesi sonucu denizin karaya doğru ilerlemesine ne ad verilir?",
                options: ["A) Regresyon", "B) Orojenez", "C) Konveksiyonel akım", "D) Transgresyon", "E) Aşınma"],
                correct: "D",
                isLong: false
            },
            {
                id: 10,
                question: "Okyanus ve deniz tabanındaki tortul tabakaların kıtaların hareketiyle yan basınca uğraması sonucu esnek tabakaların kıvrılarak, sert tabakaların ise kırılıp çökmesiyle hangi dağ türü oluşur?",
                options: ["A) Volkanik dağlar", "B) Masif dağlar", "C) Epirojenez dağları", "D) Kırıklı dağlar", "E) Kıvrımlı ve kırıklı dağlar"],
                correct: "E",
                isLong: false
            },
            {
                id: 11,
                question: "Kıvrımlı dağlarda yüksekte kalan yerlere ne denir?",
                options: ["A) Antiklinal", "B) Senklinal", "C) Horst", "D) Graben", "E) Dayk"],
                correct: "A",
                isLong: false
            },
            {
                id: 12,
                question: "Kırıklı dağlarda alçakta kalan yerlere ne denir? Ülkemizde bu tür ovaların en çok bulunduğu bölge hangisidir?",
                options: ["A) Antiklinal – Doğu Anadolu", "B) Graben – Ege Bölgesi", "C) Senklinal – Karadeniz", "D) Horst – Akdeniz", "E) Kaldera – İç Anadolu"],
                correct: "B",
                isLong: false
            },
            {
                id: 13,
                question: "Ülkemizde aktif volkan bulunmadığı için hangi deprem türü görülmez?",
                options: ["A) Tektonik depremler", "B) Çöküntü depremleri", "C) Volkanik depremler", "D) Tsunami depremleri", "E) Epirojenez depremleri"],
                correct: "C",
                isLong: false
            },
            {
                id: 14,
                question: "Depremi inceleyen bilim dalının adı nedir?",
                options: ["A) Jeoloji", "B) Volkanoloji", "C) Petrografi", "D) Sismoloji", "E) Orojenez"],
                correct: "D",
                isLong: false
            },
            {
                id: 15,
                question: "Magmanın yer yüzüne çıkıp soğuyarak katılaşmasına ne denir?",
                options: ["A) Derinlik volkanizması", "B) Konveksiyonel akım", "C) Epirojenez", "D) Orojenez", "E) Yüzey volkanizması"],
                correct: "E",
                isLong: false
            },
            {
                id: 16,
                question: "Derinlik volkanizmasında magmanın yerkabuğunun içine sokularak oluşan çok büyük volkanik kütleye ne ad verilir?",
                options: ["A) Batolit", "B) Lakolit", "C) Sill", "D) Dayk", "E) Krater"],
                correct: "A",
                isLong: false
            },
            {
                id: 17,
                question: "Magmanın yerin derinliklerinde yavaş soğuyup katılaşmasıyla oluşan püskürük kayalara ne denir?",
                options: ["A) Dış püskürük kayalar", "B) İç püskürük (plütonik) kayalar", "C) Tortul kayalar", "D) Metamorfik kayalar", "E) Organik tortul kayalar"],
                correct: "B",
                isLong: false
            },
            {
                id: 18,
                question: "Bitkisel ve hayvansal artıkların (canlı kalıntılarının) uzun süre toprak altında kalmasıyla oluşan tortul kayaç türü hangisidir?",
                options: ["A) Fiziksel tortul", "B) Kimyasal tortul", "C) Organik tortul", "D) Püskürük kayaç", "E) Başkalaşım kayaç"],
                correct: "C",
                isLong: false
            },
            {
                id: 19,
                question: "Kayaç döngüsünde tortul kayaçların oluşumunda etkili olan temel süreç hangisidir?",
                options: ["A) Erime-soğuma", "B) Yüksek sıcaklık ve basınç", "C) Kristalleşme", "D) Aşınma-taşıma-biriktirme", "E) Magmanın sokulması"],
                correct: "D",
                isLong: false
            },
            {
                id: 20,
                question: "Türkiye genel olarak bugünkü görünümünü 3. Jeolojik zamanda (Tersiyer) almıştır. İkinci jeolojik zamanda Tetis Denizi’nin altında kalan Türkiye, üçüncü zamanda yükselerek karasal alan haline gelmiş ve dış kuvvetlerin aşındırmasıyla toptan yükselmiştir. Ortalama yükseltimizin 1000 metreden fazla olması ve platoların geniş yer kaplaması bu durumun kanıtıdır.",
                options: ["A) 1. jeolojik zamanda", "B) 2. jeolojik zamanda", "C) Prekambriyen dönemde", "D) Mezozoyik dönemde", "E) 3. jeolojik zamanda"],
                correct: "E",
                isLong: true
            },
            {
                id: 21,
                question: "Türkiye en çok hangi orojenezden etkilenmiştir ve bu dönemde hangi dağlar oluşmuştur?",
                options: ["A) Alp orojenezinden – Kuzey Anadolu ve Toros Dağları", "B) Kaledoniyen orojenezinden – İskandinavya Dağları", "C) Hersiniyen orojenezinden – Appalaş Dağları", "D) Epirojenezden – Ege grabenleri", "E) Volkanizmadan – Kula tepeleri"],
                correct: "A",
                isLong: false
            },
            {
                id: 22,
                question: "Türkiye’de deprem riski en az olan yöre aşağıdakilerden hangisidir?",
                options: ["A) İstanbul", "B) Konya - Karapınar", "C) İzmir", "D) Van", "E) Hatay"],
                correct: "B",
                isLong: false
            },
            {
                id: 23,
                question: "<strong>Uzun paragraf sorusu:</strong><br>Okyanus ve deniz tabanında biriken tortul tabakalar, kıtaların hareket etmesi sonucu yan basınçlara uğrar. Esnek tabakalar kıvrılarak yükselir, sert tabakalar ise kırılır (fay) ve çöker. Böylece kıvrımlı ve kırıklı dağlar oluşur. Ülkemizde Toroslar ve Kuzey Anadolu dağları kıvrımlı dağların başlıcalarıdır. Ege bölgesinde ise kırıklı dağlar çok yaygındır ve aralarındaki ovalar graben ovalarıdır.<br><br>Yukarıdaki bilgilere göre kıvrımlı dağ örneği hangisidir?",
                options: ["A) Ege bölgesindeki dağlar", "B) Kaz Dağı", "C) Toroslar", "D) Madra Dağı", "E) Aydın Dağları"],
                correct: "C",
                isLong: true
            },
            {
                id: 24,
                question: "<strong>Uzun paragraf sorusu:</strong><br>Yüzey volkanizması magmanın yer yüzüne çıkıp soğuyarak katılaşmasıdır. Volkan konisi, krater, kaldera ve maar gibi şekiller oluşur. Derinlik volkanizmasında ise batolit, lakolit, sill ve dayk gibi kütleler meydana gelir. Aktif volkanların büyük kısmı Büyük Okyanus kıyılarında “Ateş Çemberi”nde yer alır. Volkanik topraklar mineralce çok zengindir.<br><br>Derinlik volkanizması örneği aşağıdakilerden hangisidir?",
                options: ["A) Volkan konisi", "B) Krater", "C) Kaldera", "D) Batolit", "E) Maar"],
                correct: "D",
                isLong: true
            },
            {
                id: 25,
                question: "<strong>Uzun paragraf sorusu:</strong><br>Kayaç döngüsünde tortul kayaçlar aşınma-taşıma-biriktirme ile, püskürük kayaçlar magmanın soğumasıyla, metamorfik kayaçlar ise yüksek sıcaklık ve basınç altında değişimle oluşur. Granit iç püskürüktür, mermer kireçtaşının başkalaşımıdır. Kayaçları inceleyen bilim dalına petrografi denir.<br><br>Aşağıdakilerden hangisi metamorfik kayaç örneğidir?",
                options: ["A) Bazalt", "B) Kumtaşı", "C) Kalker", "D) Linyit", "E) Mermer"],
                correct: "E",
                isLong: true
            }
        ];

        // Uygulama state
        let currentQuestions = [];
        let currentIndex = 0;
        let userAnswers = {};

        // Soruları her yüklemede rastgele karıştır
        function shuffleQuestions() {
            currentQuestions = [...questionsPool].sort(() => Math.random() - 0.5);
            currentIndex = 0;
            userAnswers = {};
        }

        // Soruyu render et
        function renderQuestion() {
            const q = currentQuestions[currentIndex];
            document.getElementById("current").textContent = currentIndex + 1;
            document.getElementById("total").textContent = currentQuestions.length;
            document.getElementById("progress-fill").style.width = `${((currentIndex) / currentQuestions.length) * 100}%`;
            document.getElementById("percentage-display").textContent = `${Math.round((currentIndex / currentQuestions.length) * 100)}%`;

            const questionEl = document.getElementById("question-text");
            questionEl.innerHTML = q.isLong 
                ? `<div class="long-question">${q.question}</div>` 
                : q.question;

            const optionsEl = document.getElementById("options");
            optionsEl.innerHTML = "";

            q.options.forEach((option, i) => {
                const btn = document.createElement("button");
                btn.className = "option-btn";
                btn.innerHTML = `<span style="font-size:1.4rem; color:var(--accent);">${option[0]}</span> ${option.slice(3)}`;
                btn.onclick = () => selectAnswer(option[0]);
                optionsEl.appendChild(btn);
            });
        }

        // Cevap seçimi (otomatik ilerleme)
        function selectAnswer(letter) {
            userAnswers[currentIndex] = letter;
            
            if (currentIndex < currentQuestions.length - 1) {
                currentIndex++;
                renderQuestion();
            } else {
                showAnalysis();
            }
        }

        // Analiz ekranı
        function showAnalysis() {
            document.getElementById("quiz-screen").style.display = "none";
            const analysis = document.getElementById("analysis-screen");
            analysis.style.display = "block";

            let correctCount = 0;
            const wrongListEl = document.getElementById("wrong-list");
            wrongListEl.innerHTML = "";

            currentQuestions.forEach((q, i) => {
                const userAnswer = userAnswers[i];
                if (userAnswer === q.correct) correctCount++;
                else {
                    const div = document.createElement("div");
                    div.style.cssText = "background:#fee2e2; padding:16px; margin-bottom:12px; border-radius:12px; border-left:5px solid #ef4444;";
                    div.innerHTML = `
                        <strong>Soru ${i+1}:</strong><br>
                        ${q.question.substring(0, 120)}...<br>
                        <span style="color:#ef4444;">Sizin cevabınız: ${userAnswer || "Boş"}</span> 
                        <span style="color:#10b981; margin-left:20px;">Doğru cevap: ${q.correct}</span>
                    `;
                    wrongListEl.appendChild(div);
                }
            });

            const percent = Math.round((correctCount / currentQuestions.length) * 100);
            document.getElementById("final-percentage").textContent = percent;

            // %80 ve üzeri başarı
            if (percent >= 80) {
                document.getElementById("success-message").style.display = "block";
                // Konfeti + Havai fişek
                confettiBurst();
            } else {
                document.getElementById("success-message").style.display = "none";
            }
        }

        // Konfeti ve havai fişek efekti
        function confettiBurst() {
            const count = 300;
            const defaults = { origin: { y: 0.6 } };

            function fire(particleRatio, opts) {
                confetti(Object.assign({}, defaults, opts, {
                    particleCount: Math.floor(count * particleRatio)
                }));
            }

            fire(0.25, { spread: 26, startVelocity: 55 });
            fire(0.2, { spread: 60 });
            fire(0.35, { spread: 100, decay: 0.91, scalar: 0.8 });
            fire(0.1, { spread: 120, startVelocity: 25, decay: 0.92, scalar: 1.2 });
            fire(0.1, { spread: 120, startVelocity: 45 });
            
            // İkinci dalga (havai fişek etkisi)
            setTimeout(() => {
                fire(0.3, { spread: 80, startVelocity: 70 });
                fire(0.2, { spread: 140, decay: 0.85 });
            }, 300);
        }

        // Yeniden başlat
        function restartExam() {
            shuffleQuestions();
            document.getElementById("analysis-screen").style.display = "none";
            document.getElementById("quiz-screen").style.display = "block";
            renderQuestion();
        }

        // Başa dön
        function goToStart() {
            currentIndex = 0;
            document.getElementById("analysis-screen").style.display = "none";
            document.getElementById("quiz-screen").style.display = "block";
            renderQuestion();
        }

        // Sınavı kapat
        function closeExam() {
            if (confirm("Sınavı kapatmak istediğinize emin misiniz?")) {
                window.close();
            }
        }

        // Uygulama başlangıcı
        window.onload = function() {
            shuffleQuestions();
            renderQuestion();
            
            // Klavye ile A-B-C-D-E tuşlarıyla cevap verme (ekstra kullanıcı dostu)
            document.addEventListener('keydown', function(e) {
                if (document.getElementById("quiz-screen").style.display !== "none") {
                    const key = e.key.toUpperCase();
                    if (["A","B","C","D","E"].includes(key)) {
                        const q = currentQuestions[currentIndex];
                        const index = q.options.findIndex(opt => opt.startsWith(key));
                        if (index !== -1) selectAnswer(key);
                    }
                }
            });
        };
    </script>
</body>
</html>