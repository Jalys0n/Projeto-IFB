import { SenhaComponent } from './senha/senha.component';
import {RouterModule, Routes} from '@angular/router';
import { CadastroUsuarioComponent } from './cadastro-usuario/cadastro-usuario.component';
import { LoginServidorComponent } from './login-servidor/login-servidor.component';
import { PaginaSenhaGeradaComponent } from './pagina-senha-gerada/pagina-senha-gerada.component';
import { PaginaFilaServidorComponent } from './pagina-fila-servidor/pagina-fila-servidor.component';
import { ModuleWithProviders } from '@angular/core';



const ROTASGERENCIADOR: Routes=[
    {path:'', component: CadastroUsuarioComponent},
    {path:'Login-Servidor', component: LoginServidorComponent},
    {path: 'sua-senha', component: PaginaSenhaGeradaComponent},
    {path:'Fila-Servidor', component: PaginaFilaServidorComponent},
    {path:'senha-monitor', component: SenhaComponent}
];

export const routing: ModuleWithProviders<RouterModule>=RouterModule. forRoot(ROTASGERENCIADOR);