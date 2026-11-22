# SD FF AI (FF ANALYSER) - Complete Native Android & Cloud Backend Architecture

**Platform**: Android 10+ (API Level 29 - 34)  
**Language**: Kotlin 1.9.22  
**UI Framework**: Jetpack Compose + Material Design 3  
**Backend & Cloud Services**: Firebase Authentication, Cloud Firestore, Firebase Cloud Storage, Cloud Functions (Node.js/TypeScript runtime with Firebase Admin & Gemini 1.5 Flash SDK), Firebase App Check.  

---

## 1. Project Directory Structure & Modular Package Layout

```text
sd-ff-ai-android/
├── build.gradle.kts (Project level)
├── settings.gradle.kts
├── gradle/wrapper/gradle-wrapper.properties
├── app/
│   ├── build.gradle.kts (App level)
│   ├── google-services.json
│   └── src/
│       ├── main/
│       │   ├── AndroidManifest.xml
│       │   ├── res/
│       │   │   ├── drawable/
│       │   │   ├── values/ (strings.xml, colors.xml, themes.xml)
│       │   │   └── mipmap/
│       │   └── java/com/sdffai/app/
│       │       ├── SdFfAiApplication.kt
│       │       ├── core/
│       │       │   ├── network/ (FirebaseClients, GeminiApiConfig)
│       │       │   ├── security/ (AppCheckProvider, TokenManager, CryptoUtils)
│       │       │   ├── util/ (DateFormatter, ResultState, RoleCategories)
│       │       │   └── theme/ (Color.kt, Type.kt, Theme.kt, Shape.kt)
│       │       ├── data/
│       │       │   ├── models/
│       │       │   │   ├── UserProfile.kt
│       │       │   │   ├── GameplayAnalysis.kt
│       │       │   │   ├── PerformanceHistory.kt
│       │       │   │   ├── TrainingPlan.kt
│       │       │   │   ├── DailyMission.kt
│       │       │   │   ├── CraftlandMap.kt
│       │       │   │   ├── Recommendations.kt
│       │       │   │   └── MetaUpdate.kt
│       │       │   └── repositories/
│       │       │       ├── AuthRepository.kt
│       │       │       ├── AnalysisRepository.kt
│       │       │       ├── TrainingRepository.kt
│       │       │       ├── MissionRepository.kt
│       │       │       ├── MetaRepository.kt
│       │       │       └── ProfileRepository.kt
│       │       ├── domain/
│       │       │   └── usecases/
│       │       │       ├── AnalyzeGameplayUseCase.kt
│       │       │       ├── CalculatePerformanceTrendsUseCase.kt
│       │       │       ├── GenerateTrainingPlanUseCase.kt
│       │       │       └── VerifyUsernameAvailabilityUseCase.kt
│       │       └── presentation/
│       │           ├── navigation/ (Screen.kt, NavGraph.kt, BottomNavBar.kt)
│       │           ├── auth/ (AuthViewModel.kt, LoginScreen.kt, OnboardingScreen.kt)
│       │           ├── dashboard/ (DashboardViewModel.kt, HomeScreen.kt, TrendCharts.kt)
│       │           ├── analysis/ (AnalysisViewModel.kt, AnalyzeScreen.kt, ReportDetailScreen.kt)
│       │           ├── training/ (TrainingViewModel.kt, TrainingScreen.kt, CraftlandMapsView.kt)
│       │           ├── meta/ (MetaViewModel.kt, MetaScreen.kt, WeaponBuildsView.kt)
│       │           └── profile/ (ProfileViewModel.kt, ProfileScreen.kt, SettingsScreen.kt)
├── backend/
│   ├── firebase.json
│   ├── firestore.rules
│   ├── storage.rules
│   ├── functions/
│   │   ├── package.json
│   │   ├── tsconfig.json
│   │   └── src/
│   │       ├── index.ts
│   │       ├── services/
│   │       │   ├── geminiAnalysisService.ts
│   │       │   ├── metaScraperService.ts
│   │       │   └── usernameLockService.ts
│   │       └── triggers/
│   │           ├── onMediaUpload.ts
│   │           └── scheduledMetaSync.ts
└── docs/
    ├── DEPLOYMENT_GUIDE.md
    ├── SECURITY_AUDIT.md
    └── FIREBASE_SETUP.md
```

---

## 2. Cloud Firestore Schema & Data Integrity Rules

### Primary Collections:

1. **`users/{uid}`**  
   - `uid`: String (Primary permanent immutable identifier)  
   - `email`: String (Verified flag required)  
   - `username`: String (Indexed lowercase)  
   - `isEmailVerified`: Boolean  
   - `linkedGoogleEmail`: String?  
   - `createdAt`: Timestamp  
   - `lastLoginAt`: Timestamp  

2. **`usernames/{usernameLower}`**  
   - `uid`: String (Transaction-locked reference to ensure 100% uniqueness without race conditions)  
   - `claimedAt`: Timestamp  

3. **`player_profiles/{uid}`**  
   - `uid`: String  
   - `isIndiaPlayer`: Boolean  
   - `isEsportsPlayer`: Boolean  
   - `selectedRoles`: Array<String> (Rusher, Sniper, Bomber, Rifler, etc. max 3)  
   - `aiSkillRating`: Number (Base scale 1000 - 3000)  
   - `totalPracticeDays`: Int  
   - `lastAnalysisDate`: Timestamp?  

4. **`gameplay_analyses/{analysisId}`**  
   - `analysisId`: String  
   - `playerUid`: String (Indexed)  
   - `mediaType`: "VIDEO" | "CLIP" | "SCREENSHOT"  
   - `mediaStorageUrl`: String  
   - `processingStatus`: "QUEUED" | "PROCESSING" | "COMPLETED" | "FAILED"  
   - `isVerifiedMatchData`: Boolean  
   - `accuracyRate`: Float  
   - `headshotRate`: Float  
   - `kdRatioEstimate`: Float?  
   - `movementScore`: Float  
   - `strengths`: List<String>  
   - `weaknesses`: List<String>  
   - `detectedMistakes`: List<String>  
   - `improvementDrills`: List<String>  
   - `roleObservations`: String  
   - `createdAt`: Timestamp  

5. **`performance_history/{uid}/snapshots/{snapshotId}`**  
   - Aggregated metrics per 3D, 7D, 14D, 30D, 60D, 90D, 180D intervals.  
   - Stores delta percentages (+4.2% HS Rate, -1.8% Survival Time) and trend statuses.  

6. **`daily_missions/{uid}/active/{missionId}`**  
   - Role-adapted tasks (e.g., Rusher: "Execute 15 Close-Range Quick Gloo Wall Drops", Sniper: "Maintain 65%+ Crosshair Center Alignment").  
   - `targetCount`: Int, `currentProgress`: Int, `xpReward`: Int, `isCompleted`: Boolean.  

7. **`craftland_maps/{mapId}`**  
   - `mapName`: String  
   - `mapCode`: String  
   - `category`: "AIM_PRACTICE" | "GLOO_WALL_FAST" | "SNIPER_PEEK" | "RUSH_ZONE"  
   - `serverRegion`: "INDIA" | "GLOBAL"  
   - `isVerified`: Boolean  
   - `verificationDate`: Timestamp  

8. **`meta_updates/{updateId}`**  
   - Real-time verified patch notes, weapon damage balance charts, character skill rework data.  

---

## 3. Firebase Security Rules (`firestore.rules`)

```javascript
rules_version = '2';
service cloud.firestore {
  match /databases/{database}/documents {
    
    // User check helper
    function isAuthenticated() {
      return request.auth != null;
    }
    function isOwner(userId) {
      return isAuthenticated() && request.auth.uid == userId;
    }

    // User Profile: Only accessible by user owner
    match /users/{userId} {
      allow read: if isOwner(userId);
      allow create: if isAuthenticated() && request.auth.uid == userId;
      allow update: if isOwner(userId) && !request.resource.data.diff(resource.data).affectedKeys().hasAny(['uid']);
      allow delete: if false; // Clean deletion handled via Cloud Function
    }

    // Global unique username lookup
    match /usernames/{username} {
      allow read: if isAuthenticated();
      allow create, delete: if isAuthenticated(); 
    }

    // Player profiles & private performance history
    match /player_profiles/{userId} {
      allow read, write: if isOwner(userId);
    }
    
    match /performance_history/{userId}/{document=**} {
      allow read, write: if isOwner(userId);
    }

    // Analyses: Read & Create only own data, prevent modifying completed stats
    match /gameplay_analyses/{analysisId} {
      allow read: if isAuthenticated() && resource.data.playerUid == request.auth.uid;
      allow create: if isAuthenticated() && request.resource.data.playerUid == request.auth.uid;
      allow update: if false; // Only Cloud Functions can update analysis results
    }

    // Missions
    match /daily_missions/{userId}/{document=**} {
      allow read, write: if isOwner(userId);
    }

    // Public verified info (Craftland maps & Meta updates)
    match /craftland_maps/{mapId} {
      allow read: if isAuthenticated();
      allow write: if false; // Admin managed
    }
    match /meta_updates/{updateId} {
      allow read: if isAuthenticated();
      allow write: if false; // Admin managed
    }
  }
}
```

---

## 4. Secure Backend Logic & Gemini Integration (`backend/functions/src/services/geminiAnalysisService.ts`)

```typescript
import { GoogleGenerativeAI } from "@google/generative-ai";
import * as admin from "firebase-admin";

const genAI = new GoogleGenerativeAI(process.env.GEMINI_API_KEY || "");

export interface GameplayAnalysisRequest {
  analysisId: string;
  playerUid: string;
  mediaUrl: string;
  mediaType: "VIDEO" | "CLIP" | "SCREENSHOT";
  playerRole: string;
}

export async function processGameplayMedia(req: GameplayAnalysisRequest) {
  const model = genAI.getGenerativeModel({ model: "gemini-1.5-flash" });

  const prompt = `
You are SD FF AI, an elite Free Fire Esports Performance Analyst and Coach.
Analyze the provided ${req.mediaType} for a player assigned the role: ${req.playerRole}.

CRITICAL RULES:
1. Never fabricate kills, deaths, or match statistics that are not clearly visible.
2. If it is a screenshot, evaluate visible HUD stats, positioning, crosshair placement, weapon combos, and layout. Explicitly declare movement or decision-making as "Inferred/Not determinable from single frame".
3. Distinguish between directly detected facts vs AI coach estimations.
4. Output response strictly in JSON format matching this schema:
{
  "accuracyRate": number (0-100),
  "headshotRate": number (0-100),
  "movementScore": number (0-100),
  "isVerifiedMatchData": boolean,
  "strengths": string[],
  "weaknesses": string[],
  "detectedMistakes": string[],
  "improvementDrills": string[],
  "roleObservations": string,
  "summary": string
}
`;

  try {
    const result = await model.generateContent([
      prompt,
      {
        fileData: {
          mimeType: req.mediaType === "SCREENSHOT" ? "image/jpeg" : "video/mp4",
          fileUri: req.mediaUrl,
        },
      },
    ]);

    const responseText = result.response.text();
    const cleanJson = responseText.replace(/```json|```/g, "").trim();
    const parsedData = JSON.parse(cleanJson);

    // Save strictly validated data into Firestore
    await admin.firestore().collection("gameplay_analyses").doc(req.analysisId).update({
      ...parsedData,
      processingStatus: "COMPLETED",
      completedAt: admin.firestore.FieldValue.serverTimestamp(),
    });

  } catch (error) {
    console.error("Analysis failed:", error);
    await admin.firestore().collection("gameplay_analyses").doc(req.analysisId).update({
      processingStatus: "FAILED",
      errorMessage: "AI Analysis Engine was unable to process this media.",
    });
  }
}
```

---

## 5. Build, APK Generation & Deployment Guide

### A. Android Build (Gradle / Command Line)
```bash
# Clean project
./gradlew clean

# Build Debug APK
./gradlew assembleDebug
# Generated at: app/build/outputs/apk/debug/app-debug.apk

# Build Signed Release APK
./gradlew assembleRelease
# Generated at: app/build/outputs/apk/release/app-release.apk
```

### B. Firebase Backend Deployment
```bash
npm install -g firebase-tools
firebase login
firebase use --add <your-firebase-project-id>
firebase deploy --only firestore:rules,storage:rules,functions
```
