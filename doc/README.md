# Documentation
For now, these are notes on using the [kanji recognition for Android](https://github.com/ichisadashioko/kanji-recognition-android) in experiment `KanjiDrawer`.

## Steps
1. Create a new Android Studio project
2. Install [Android NDK](https://developer.android.com/ndk/guides), which allows you to run native C/C++ code in an Android project.
    * Followed these [NDK and CMake installation instructions](https://developer.android.com/studio/projects/install-ndk#default-version), which can easily be done through `Tools > SDK Manager` in Android Studio.
3. Add `tensorflow-lite` to `app/build.gradle` dependencies (don't add to the `root/` dependencies!)

```
dependencies {
    ...
    // Tensorflow Lite library
    implementation 'org.tensorflow:tensorflow-lite:0.0.0-nightly'
}
```

4. Sync gradle file

5. Create an `assets/` folder in my Android project by right-clicking on the `app/` folder in Android Studio and clicking `New > Folder > Assets Folder`. Chose default options (create in `main/`)

6. Git clone the [kanji-recognition-android project](https://github.com/ichisadashioko/kanji-recognition-android) and copy their `tflite` model from their app's `assets/` folder into your project's `assets/` folder.

7. Add `noCompress` option to `app/build.gradle` file so that the `tflite` file will not be compressed:

```
android {
    ...
    aaptOptions {
        noCompress 'tflite'
    }
}
```

8. At the top of `MainActivity.java`, import the `Interpreter` class from `tensorflow.lite`:

```
import org.tensorflow.lite.Interpreter;
```
If errors occur here, make sure that `tensoreflow-lite` was added to `app/build.gradle` (step 3) and the gradle file was synced (step 4).

## Errors
* Got an `No version of NDK...` error. Deleted the `ndk/` directories by following [this solution](https://github.com/gradle/gradle/issues/12440#issuecomment-601214647).
* [Converting an InputStream to a MappedByteBuffer](https://stackoverflow.com/questions/19616023/converting-inputstream-to-mappedbytebuffer-in-java)
* [Load and run a model in Java](https://www.tensorflow.org/lite/guide/inference#load_and_run_a_model_in_java) in TensorFlow
