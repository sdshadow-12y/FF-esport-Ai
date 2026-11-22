# SD FF AI (FF ANALYSER) — Production Android APK Build & Release Guide

**Package Name**: `com.sdffai.app`  
**Target Platform**: Android 10+ (API Level 29 - 34)  
**Build System**: Gradle Kotlin DSL (`build.gradle.kts`)  
**Architecture**: Clean Architecture + MVVM + Jetpack Compose  
**Output Target**: Production Signed Release APK & Debug APK

---

## 1. Prerequisites & Environment Setup

Ensure the following tools are installed in your development environment:
- **Android Studio Iguana | 2023.2.1** (or Ladybug / newer)
- **JDK 17** (Temurin / OpenJDK 17 recommended)
- **Android SDK API 34** with SDK Build-Tools `34.0.0`
- **Gradle 8.4** (or bundled Gradle Wrapper 8.4)
- **`google-services.json`** placed in the `app/` directory (from Firebase Console)

Verify environment variables:
```bash
export ANDROID_HOME=$HOME/Android/Sdk
export PATH=$PATH:$ANDROID_HOME/tools:$ANDROID_HOME/platform-tools
export JAVA_HOME=/Library/Java/JavaVirtualMachines/temurin-17.jdk/Contents/Home
```

---

## 2. Generating a Secure Release Keystore

Before compiling the production release APK, generate a cryptographic keystore:

```bash
keytool -genkey -v \
  -keystore sdffai-release-key.jks \
  -alias sdffai_release \
  -keyalg RSA \
  -keysize 2048 \
  -validity 10000 \
  -storetype JKS
```

Create a secure `keystore.properties` file in your project root (ensure this is added to `.gitignore`):
```properties
RELEASE_STORE_FILE=../sdffai-release-key.jks
RELEASE_STORE_PASSWORD=your_keystore_password
RELEASE_KEY_ALIAS=sdffai_release
RELEASE_KEY_PASSWORD=your_key_password
```

---

## 3. App-Level Build Configuration (`app/build.gradle.kts`)

Verify that your `app/build.gradle.kts` specifies signing and optimization configs:

```kotlin
import java.util.Properties
import java.io.FileInputStream

plugins {
    alias(libs.plugins.android.application)
    alias(libs.plugins.kotlin.android)
    alias(libs.plugins.google.gms.services)
    alias(libs.plugins.kotlin.kapt)
    alias(libs.plugins.hilt.android)
}

val keystorePropertiesFile = rootProject.file("keystore.properties")
val keystoreProperties = Properties().apply {
    if (keystorePropertiesFile.exists()) {
        load(FileInputStream(keystorePropertiesFile))
    }
}

android {
    namespace = "com.sdffai.app"
    compileSdk = 34

    defaultConfig {
        applicationId = "com.sdffai.app"
        minSdk = 29
        targetSdk = 34
        versionCode = 100
        versionName = "1.0.0-OB45"

        testInstrumentationRunner = "androidx.test.runner.AndroidJUnitRunner"
        vectorDrawables {
            useSupportLibrary = true
        }
    }

    signingConfigs {
        create("release") {
            storeFile = file(keystoreProperties.getProperty("RELEASE_STORE_FILE") ?: "sdffai-release-key.jks")
            storePassword = keystoreProperties.getProperty("RELEASE_STORE_PASSWORD")
            keyAlias = keystoreProperties.getProperty("RELEASE_KEY_ALIAS")
            keyPassword = keystoreProperties.getProperty("RELEASE_KEY_PASSWORD")
            enableV1Signing = true
            enableV2Signing = true
        }
    }

    buildTypes {
        release {
            isMinifyEnabled = true
            isShrinkResources = true
            proguardFiles(
                getDefaultProguardFile("proguard-android-optimize.txt"),
                "proguard-rules.pro"
            )
            signingConfig = signingConfigs.getByName("release")
        }
        debug {
            applicationIdSuffix = ".debug"
            isDebuggable = true
        }
    }

    compileOptions {
        sourceCompatibility = JavaVersion.VERSION_17
        targetCompatibility = JavaVersion.VERSION_17
    }

    kotlinOptions {
        jvmTarget = "17"
        freeCompilerArgs += listOf(
            "-opt-in=androidx.compose.material3.ExperimentalMaterial3Api",
            "-opt-in=kotlinx.coroutines.ExperimentalCoroutinesApi"
        )
    }

    buildFeatures {
        compose = true
        buildConfig = true
    }

    composeOptions {
        kotlinCompilerExtensionVersion = "1.5.8"
    }

    packaging {
        resources {
            excludes += "/META-INF/{AL2.0,LGPL2.1}"
        }
    }
}
```

---

## 4. ProGuard / R8 Obfuscation & Hardening Rules (`app/proguard-rules.pro`)

To prevent reverse engineering of proprietary Free Fire esports scoring algorithms:

```proguard
# Jetpack Compose Rules
-keepattributes *Annotation*
-dontwarn androidx.compose.**

# Firebase SDKs
-keep class com.google.firebase.** { *; }
-dontwarn com.google.firebase.**

# Kotlin Coroutines & Flow
-keepnames class kotlinx.coroutines.internal.MainDispatcherFactory {}
-keepnames class kotlinx.coroutines.CoroutineExceptionHandler {}

# Gemini SDK and Data Models
-keepclassmembers class com.sdffai.app.data.models.** { *; }
-keepclassmembers enum com.sdffai.app.data.models.** { *; }

# OkHttp & Retrofit Network Serialization
-keepattributes Signature
-keepattributes InnerClasses
-dontwarn okhttp3.**
-dontwarn okio.**
```

---

## 5. Build Commands (Terminal Execution)

Run these commands from the project root directory:

### A. Clean Build Cache
```bash
./gradlew clean
```

### B. Compile & Assemble Debug APK (Immediate Testing)
```bash
./gradlew assembleDebug
```
*Generated output location*:  
`app/build/outputs/apk/debug/app-debug.apk`

### C. Compile & Assemble Production Signed Release APK
```bash
./gradlew assembleRelease
```
*Generated output location*:  
`app/build/outputs/apk/release/app-release.apk`

### D. Compile Android App Bundle (.aab) for Google Play Console
```bash
./gradlew bundleRelease
```
*Generated output location*:  
`app/build/outputs/bundle/release/app-release.aab`

---

## 6. Sideloading & Verification via ADB

To test the generated APK directly on a connected physical Android device or emulator:

```bash
# 1. Verify connected device
adb devices

# 2. Install debug APK with replace flag
adb install -r app/build/outputs/apk/debug/app-debug.apk

# 3. Launch the app directly into Onboarding / Dashboard
adb shell am start -n com.sdffai.app/com.sdffai.app.presentation.MainActivity

# 4. Stream real-time logcat output filtered for SD FF AI
adb logcat -s "SdFfAi" "GeminiAnalysis" "FirestoreSecurity"
```

---

## 7. APK Quality & Pre-Flight Checklist

- [x] **Firebase Connection**: `google-services.json` verified with SHA-1 and SHA-256 fingerprints registered in Firebase Console.
- [x] **Play Integrity / App Check**: Production token provider configured for anti-tamper security.
- [x] **Firestore Security Rules**: Rules deployed (`firebase deploy --only firestore:rules`) locking AI stat modifications.
- [x] **Verified Weapon PNGs**: All 10 official Free Fire weapon PNG assets bundled into `res/drawable-nodpi/` for high-density rendering.
- [x] **V1 & V2 APK Signature**: Dual signature scheme validated via `apksigner verify --verbose app-release.apk`.
