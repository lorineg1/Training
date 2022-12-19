import { Component } from '@angular/core';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent {
  title = 'Mazal Tov';
  bracha = "כל הכבוד על עליית האתר. אתם בחצי הדרך בלסיים את הפרק ועוד מעט תיכנסו לצוות אומגה";
  end = "וכמו שחוכמי אומגה אמרו: 'בחורה לחתונה מוצאים רק בספריה' ע.ר"
  checkwebhook = "Hello im checking this webhook third time"
}
