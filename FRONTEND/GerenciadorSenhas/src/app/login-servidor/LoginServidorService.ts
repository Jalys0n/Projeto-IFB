import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root',
})
export class LoginServidorService {
  private apiUrl = 'http://localhost:5000';

  constructor(private http: HttpClient) {}

  loginServidor(cpfServidor: number, senhaServidor: string, guicheServidor: string): Observable<any> {
    const payload = {
      cpf_servidor: cpfServidor,
      senha_servidor: senhaServidor,
      guiche_servidor: guicheServidor,
    };

    return this.http.post(`${this.apiUrl}/login-servidor`, payload);
  }
}
