import { Routes } from '@angular/router';
import { EmotionFormComponent } from './emotion-form/emotion-form.component';

export const routes: Routes = [
  { path: '', component: EmotionFormComponent }, // default route
  { path: '**', redirectTo: '' } // wildcard route to redirect unknown paths
];
