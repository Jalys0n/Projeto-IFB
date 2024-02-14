import { Component, OnInit } from '@angular/core';
import { ApiService } from '../app.service';
import {Router} from '@angular/router';

@Component({
  selector: 'app-cadastro-usuario',
  templateUrl: './cadastro-usuario.component.html',
  styleUrls: ['./cadastro-usuario.component.css']
})
export class CadastroUsuarioComponent implements OnInit {
  assuntos: any[] = [];
  tiposUsuarios: any[] = [];
  nomeUsuario: string = '';
  cpf: string = '';
  assunto: string = '';
  comunidade: string = '';
  preferencia: string = '';

  constructor(private apiService: ApiService, private router:Router) {}

  ngOnInit(): void {
    console.log('ngOnInit foi chamado!');
    this.carregarAssuntos();
    this.carregarTiposUsuarios();
  }
  
  cadastrarUsuario() {

    const dadosCadastro = {
      nomeUsuario: this.nomeUsuario,
      cpf: this.cpf,
      assunto: this.assunto,
      comunidade: this.comunidade,
      preferencia: this.preferencia
    };
    this.apiService.cadastrarUsuario(dadosCadastro).subscribe(
      (data: any) => {
        this.router.navigate(['/sua-senha'], { queryParams: { senha: data.senha } });
      },
      (error:any) => {
        console.error('Erro ao cadastrar usuário:', error);
      }
    );
  }

  carregarAssuntos() {
    this.apiService.getAssuntos().subscribe(
      (data) => {
        this.assuntos = data;
        console.log('Assuntos carregados:', this.assuntos);
      },
      (error) => {
        console.error('Erro ao obter assuntos:', error);
      }
    );
  }

  carregarTiposUsuarios() {
    this.apiService.getTiposUsuarios().subscribe(
      (data) => {
        this.tiposUsuarios = data;
        console.log('Tipos de usuários carregados:', this.tiposUsuarios);
      },
      (error) => {
        console.error('Erro ao obter tipos de usuários:', error);
      }
    );
  }
}
