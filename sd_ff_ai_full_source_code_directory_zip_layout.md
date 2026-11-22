# SD FF AI (FF ANALYSER) — Complete Production Source Code Archive Manifest & ZIP File Tree Structure

**Package**: `com.sdffai.app`  
**Target Platform**: Android 10+ (API Level 29 - 34)  
**Architecture**: Clean Architecture + MVVM + Jetpack Compose + Firebase & Gemini Cloud Backend  
**Archive Target**: `sd-ff-ai-production-v1.0.0.zip`

---

## 1. Complete Source Code Directory Tree Layout (ZIP Structure)

```text
sd-ff-ai-android/
├── .gitignore
├── README.md
├── build.gradle.kts
├── settings.gradle.kts
├── gradle.properties
├── keystore.properties.example
├── gradlew
├── gradlew.bat
├── gradle/
│   └── wrapper/
│       ├── gradle-wrapper.jar
│       └── gradle-wrapper.properties
│
├── app/
│   ├── .gitignore
│   ├── build.gradle.kts
│   ├── proguard-rules.pro
│   ├── google-services.json
│   └── src/
│       ├── main/
│       │   ├── AndroidManifest.xml
│       │   ├── res/
│       │   │   ├── drawable-nodpi/
│       │   │   │   ├── trogon.png
│       │   │   │   ├── mag7.png
│       │   │   │   ├── charge_buster.png
│       │   │   │   ├── m590.png
│       │   │   │   ├── skorp.png
│       │   │   │   ├── mp5_chip3.png
│       │   │   │   ├── kord.png
│       │   │   │   ├── m60.png
│       │   │   │   ├── awm.png
│       │   │   │   ├── m82b.png
│       │   │   │   ├── bizon.png
│       │   │   │   ├── thompson.png
│       │   │   │   ├── p90.png
│       │   │   │   ├── hawk_hawk.png
│       │   │   │   ├── vsk94.png
│       │   │   │   ├── woodpecker.png
│       │   │   │   ├── svd.png
│       │   │   │   ├── ac80.png
│       │   │   │   └── sks.png
│       │   │   ├── drawable/
│       │   │   │   ├── ic_launcher_background.xml
│       │   │   │   ├── ic_launcher_foreground.xml
│       │   │   │   └── ic_crosshair_hud.xml
│       │   │   ├── mipmap-xxxhdpi/
│       │   │   │   ├── ic_launcher.webp
│       │   │   │   └── ic_launcher_round.webp
│       │   │   └── values/
│       │   │       ├── strings.xml
│       │   │       ├── colors.xml
│       │   │       └── themes.xml
│       │   └── java/com/sdffai/app/
│       │       ├── SdFfAiApplication.kt
│       │       │
│       │       ├── core/
│       │       │   ├── di/
│       │       │   │   ├── AppModule.kt
│       │       │   │   ├── FirebaseModule.kt
│       │       │   │   └── RepositoryModule.kt
│       │       │   ├── network/
│       │       │   │   ├── FirebaseClients.kt
│       │       │   │   └── GeminiApiConfig.kt
│       │       │   ├── security/
│       │       │   │   ├── AppCheckProvider.kt
│       │       │   │   └── TokenManager.kt
│       │       │   ├── util/
│       │       │   │   ├── ResultState.kt
│       │       │   │   ├── RoleConstants.kt
│       │       │   │   └── Ob45WeaponSpecs.kt
│       │       │   └── theme/
│       │       │       ├── Color.kt
│       │       │       ├── Type.kt
│       │       │       ├── Shape.kt
│       │       │       └── Theme.kt
│       │       │
│       │       ├── data/
│       │       │   ├── models/
│       │       │   │   ├── UserProfile.kt
│       │       │   │   ├── GameplayAnalysis.kt
│       │       │   │   ├── SquadRoster.kt
│       │       │   │   ├── WeaponItem.kt
│       │       │   │   ├── DailyMission.kt
│       │       │   │   ├── CraftlandMap.kt
│       │       │   │   └── MetaUpdate.kt
│       │       │   └── repositories/
│       │       │       ├── AuthRepository.kt
│       │       │       ├── AuthRepositoryImpl.kt
│       │       │       ├── AnalysisRepository.kt
│       │       │       ├── AnalysisRepositoryImpl.kt
│       │       │       ├── SquadRosterRepository.kt
│       │       │       ├── SquadRosterRepositoryImpl.kt
│       │       │       ├── TrainingRepository.kt
│       │       │       ├── TrainingRepositoryImpl.kt
│       │       │       ├── MetaRepository.kt
│       │       │       └── MetaRepositoryImpl.kt
│       │       │
│       │       ├── domain/
│       │       │   └── usecases/
│       │       │       ├── AnalyzeGameplayUseCase.kt
│       │       │       ├── GetSquadRosterUseCase.kt
│       │       │       ├── UpdatePlayerRoleUseCase.kt
│       │       │       ├── FetchCraftlandMapsUseCase.kt
│       │       │       └── FetchMetaUpdatesUseCase.kt
│       │       │
│       │       └── presentation/
│       │           ├── MainActivity.kt
│       │           ├── navigation/
│       │           │   ├── Screen.kt
│       │           │   ├── NavGraph.kt
│       │           │   └── BottomNavBar.kt
│       │           ├── common/
│       │           │   ├── TopAppBar.kt
│       │           │   ├── WeaponCard.kt
│       │           │   ├── StatBadge.kt
│       │           │   └── EsportsRadarChart.kt
│       │           ├── onboarding/
│       │           │   ├── OnboardingViewModel.kt
│       │           │   ├── OnboardingScreen.kt
│       │           │   └── BentoRoleGrid.kt
│       │           ├── dashboard/
│       │           │   ├── DashboardViewModel.kt
│       │           │   ├── HomeScreen.kt
│       │           │   └── TrendMetricsView.kt
│       │           ├── analysis/
│       │           │   ├── AnalysisViewModel.kt
│       │           │   ├── AnalyzeScreen.kt
│       │           │   └── ReportDetailScreen.kt
│       │           ├── squad/
│       │           │   ├── SquadWeaponViewModel.kt
│       │           │   ├── SquadAllocationScreen.kt
│       │           │   └── AttachmentDialog.kt
│       │           ├── training/
│       │           │   ├── TrainingViewModel.kt
│       │           │   ├── TrainingScreen.kt
│       │           │   └── CraftlandMapView.kt
│       │           ├── meta/
│       │           │   ├── MetaViewModel.kt
│       │           │   ├── MetaScreen.kt
│       │           │   └── WeaponCompendiumView.kt
│       │           └── profile/
│       │               ├── ProfileViewModel.kt
│       │               ├── ProfileScreen.kt
│       │               └── RoleSwapDialog.kt
│       │
│       └── test/
│           └── java/com/sdffai/app/
│               ├── AnalysisRepositoryTest.kt
│               └── SquadRosterCalculationTest.kt
│
├── backend/
│   ├── firebase.json
│   ├── firestore.rules
│   ├── firestore.indexes.json
│   ├── storage.rules
│   └── functions/
│       ├── package.json
│       ├── tsconfig.json
│       └── src/
│           ├── index.ts
│           ├── services/
│           │   ├── geminiAnalysisService.ts
│           │   ├── usernameLockService.ts
│           │   └── metaSyncService.ts
│           └── triggers/
│               ├── onMediaUploaded.ts
│               └── scheduledMetaSync.ts
│
└── scripts/
    ├── package_source_zip.sh
    ├── build_debug_apk.sh
    └── build_release_apk.sh
```

---

## 2. Shell Packaging Script (`scripts/package_source_zip.sh`)

You can run this script in your root directory to instantly create a clean, reproducible ZIP archive excluding build caches:

```bash
#!/usr/bin/env bash
set -e

ARCHIVE_NAME="sd-ff-ai-production-v1.0.0.zip"

echo "=== Packaging SD FF AI Android Source Code into ${ARCHIVE_NAME} ==="

# Clean build artifacts first
./gradlew clean || true

# Create zip archive excluding build dirs, keystores, and caches
zip -r "${ARCHIVE_NAME}" . \
  -x "*.git*" \
  -x "*.gradle*" \
  -x "*/build/*" \
  -x "*.idea*" \
  -x "*.DS_Store" \
  -x "sdffai-release-key.jks" \
  -x "keystore.properties" \
  -x "backend/functions/node_modules/*" \
  -x "backend/functions/lib/*"

echo "=== Complete! ${ARCHIVE_NAME} created successfully ==="
unzip -l "${ARCHIVE_NAME}" | head -n 35
```

---

## 3. Core Android Manifest (`app/src/main/AndroidManifest.xml`)

```xml
<?xml version="1.0" encoding="utf-8"?>
<manifest xmlns:android="http://schemas.android.com/apk/res/android"
    xmlns:tools="http://schemas.android.com/tools"
    package="com.sdffai.app">

    <!-- Permissions required for AI Gameplay Analysis & Firebase Sync -->
    <uses-permission android:name="android.permission.INTERNET" />
    <uses-permission android:name="android.permission.ACCESS_NETWORK_STATE" />
    <uses-permission android:name="android.permission.READ_MEDIA_IMAGES" />
    <uses-permission android:name="android.permission.READ_MEDIA_VIDEO" />
    <uses-permission android:name="android.permission.READ_EXTERNAL_STORAGE" 
        android:maxSdkVersion="32" />

    <application
        android:name=".SdFfAiApplication"
        android:allowBackup="false"
        android:icon="@mipmap/ic_launcher"
        android:label="@string/app_name"
        android:roundIcon="@mipmap/ic_launcher_round"
        android:supportsRtl="true"
        android:theme="@style/Theme.SdFfAi"
        android:usesCleartextTraffic="false"
        tools:targetApi="34">

        <activity
            android:name=".presentation.MainActivity"
            android:exported="true"
            android:screenOrientation="portrait"
            android:windowSoftInputMode="adjustResize"
            android:theme="@style/Theme.SdFfAi">
            <intent-filter>
                <action android:name="android.intent.action.MAIN" />
                <category android:name="android.intent.category.LAUNCHER" />
            </intent-filter>
        </activity>

    </application>
</manifest>
```

---

## 4. Root Gradle Build Configuration (`build.gradle.kts`)

```kotlin
// Top-level build file where you can add configuration options common to all sub-projects/modules.
plugins {
    alias(libs.plugins.android.application) apply false
    alias(libs.plugins.kotlin.android) apply false
    alias(libs.plugins.google.gms.services) apply false
    alias(libs.plugins.hilt.android) apply false
}

tasks.register("clean", Delete::class) {
    delete(rootProject.layout.buildDirectory)
}
```

---

## 5. Summary of Verified Assets Bundled in `res/drawable-nodpi/`

All 10 official Free Fire weapons verified during calibration are mapped into this directory tree:

| File Name | Gun Name | Category | Role Association |
| :--- | :--- | :--- | :--- |
| `trogon.png` | **Trogon** | Shotgun / Grenade Dual | Role 01 (Primary Rusher) |
| `skorp.png` | **SKORP** | SMG | Role 01 (Secondary Rusher) |
| `mag7.png` | **MAG-7** | Tactical Shotgun | Role 02 (Secondary Rusher) |
| `mp5_chip3.png` | **MP5 Chip III** | SMG | Role 02 (Secondary Rusher) |
| `charge_buster.png` | **Charge Buster** | Kinetic Shotgun | Role 03 (Combat Bomber) |
| `m590.png` | **M590** | Tactical Breacher Shotgun | Role 03 (Breacher Option) |
| `kord.png` | **KORD** | Light Machine Gun | Role 04 (Assaulter Support) |
| `m60.png` | **M60** | Light Machine Gun | Role 04 (Heavy Suppression) |
| `awm.png` | **AWM (.50 Magnum)** | Bolt-Action Sniper | Role 05 (Precision Overwatch) |
| `m82b.png` | **M82B Barrett** | Anti-Material Sniper | Role 05 (Gloo Wall Penetration) |
