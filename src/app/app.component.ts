import { Component } from '@angular/core';
import { RouterOutlet } from '@angular/router';
import { EmotionFormComponent } from './emotion-form/emotion-form.component';
import { MatCard } from "@angular/material/card";

@Component({
  selector: 'app-root',
  imports: [
    EmotionFormComponent,
    MatCard,
    RouterOutlet
],
  templateUrl: './app.component.html',
  styleUrl: './app.component.css'
})
export class AppComponent {
  title = 'mood-reader';
}
