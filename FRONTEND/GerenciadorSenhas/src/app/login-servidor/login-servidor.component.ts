import { Component } from '@angular/core';
import { LoginServidorService } from './LoginServidorService'; 
import { Router } from '@angular/router';

@Component({
  selector: 'app-login-servidor',
  templateUrl: './login-servidor.component.html',
  styleUrls: ['./login-servidor.component.css']
})
export class LoginServidorComponent {
  constructor(private loginServidorService: LoginServidorService, private router: Router) {}

  onSubmit(cpfServidor: string, senhaServidor: string, guicheServidor: string): void {
    const cpfNumber = parseInt(cpfServidor, 10); // ou parseFloat, dependendo da sua necessidade

    this.loginServidorService.loginServidor(cpfNumber, senhaServidor, guicheServidor).subscribe(
      (response) => {
        console.log('Login bem-sucedido:', response);
        this.router.navigate(['/Fila-Servidor']);
      },
      (error) => {
        console.error('Erro no login:', error);
        alert('Erro no login, verifique os dados e tente novamente');
      }
    );
  }
}
