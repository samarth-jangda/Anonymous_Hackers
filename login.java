package com.example.codingshaft;

import androidx.appcompat.app.AppCompatActivity;

import android.content.Intent;
import android.net.Uri;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
import android.widget.Toast;

public class Login extends AppCompatActivity {
    EditText e1,e2;
    Button b1,b3,b4;
    DatabaseHelper db;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_login);
        db=new DatabaseHelper(this);
        e1=findViewById(R.id.editText);
        e2=findViewById(R.id.editText2);
        b1=findViewById(R.id.button);
        b1.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                String email=e1.getText().toString();
                String password=e2.getText().toString();
                Boolean chkemailpass=db.emailpassword(email,password);
                if (chkemailpass==true){
                    Uri uri = Uri.parse("https://forms.gle/kMmSExFBwrV9LzSE8");
                    Intent intent = new Intent(Intent.ACTION_VIEW, uri);
                    startActivity(intent);
                   // Intent i=new Intent(Login.this,Course.class);
                    //startActivity(i);
                    Toast.makeText(getApplicationContext(),"Successfully Login",Toast.LENGTH_SHORT).show();

                }
                else {
                    Toast.makeText(getApplicationContext(),"Login Failed",Toast.LENGTH_SHORT).show();
                }
                e1.setText("");
                e2.setText("");


            }
        });

    }
}
