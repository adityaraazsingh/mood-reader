import { Component } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';
import { HttpClient, HttpClientModule } from '@angular/common/http';
import { result } from '../bo/result';
import { MatCardModule } from '@angular/material/card';

@Component({
  selector: 'app-emotion-form',
  standalone: true,
  imports: [CommonModule, FormsModule, MatCardModule, HttpClientModule],
  templateUrl: './emotion-form.component.html',
  styleUrls: ['./emotion-form.component.css']
})
export class EmotionFormComponent {
  inputText = '';
  result: result | null = null;
  color : string | undefined = '' ;


  
  constructor(private http: HttpClient) {}

// http://localhost:8000/analyze

  submitText() {
  this.http.post<any>('https://mood-reader-api.onrender.com/analyze', { text: this.inputText })
    .subscribe({
      next: (res) => {
        this.result = res;
        this.color = res.color_code; 
      },
      error: (err) => console.error('Error:', err)
    });
}

}
