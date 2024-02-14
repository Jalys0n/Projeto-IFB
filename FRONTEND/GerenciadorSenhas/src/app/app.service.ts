import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root',
})
export class ApiService {
  private apiUrl = 'http://localhost:5000';

  constructor(private http: HttpClient) {}

  getAssuntos(): Observable<any[]> {
    return this.http.get<any[]>(`${this.apiUrl}/obter-atendimentos`);
  }

  getTiposUsuarios(): Observable<any[]> {
    return this.http.get<any[]>(`${this.apiUrl}/tipo-usuario`);
  }

  cadastrarUsuario(dadosUsuario: any): Observable<any> {
    const url = `${this.apiUrl}/cadastro`; 
    
    return this.http.post<any>(url, dadosUsuario);
  }
}
