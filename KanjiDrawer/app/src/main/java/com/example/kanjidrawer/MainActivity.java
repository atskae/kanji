package com.example.kanjidrawer;

import androidx.appcompat.app.AppCompatActivity;

import android.os.Bundle;
import android.util.Log;

import org.tensorflow.lite.Interpreter;
import java.io.File;
import java.io.FileInputStream;
import java.io.InputStream;
import java.nio.ByteBuffer;
import java.nio.channels.FileChannel;

public class MainActivity extends AppCompatActivity {

    private Interpreter it; // kanji interpreter

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        String model_filename = getResources().getString(R.string.model_filename);
        Log.i("MainActivity", "Creating an Interpreter " + model_filename);
        try {
            InputStream is = getAssets().open(model_filename);
            FileInputStream fis = (FileInputStream) is;
            FileChannel channel = fis.getChannel();
            ByteBuffer buffer = channel.map(FileChannel.MapMode.READ_ONLY, 0, channel.size());
            this.it = new Interpreter(buffer);
            Log.i("MainActivity", "Successfully created an Interpreter using " + model_filename);
        } catch (Exception e) {
            Log.e("MainActivity", "Failed to open model file " + model_filename, e);
        }
        Log.i("MainActivity", "Done.");
    }
}