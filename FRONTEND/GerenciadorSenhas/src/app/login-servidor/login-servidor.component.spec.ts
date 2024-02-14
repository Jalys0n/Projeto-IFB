import { ComponentFixture, TestBed } from '@angular/core/testing';

import { LoginServidorComponent } from './login-servidor.component';

describe('LoginServidorComponent', () => {
  let component: LoginServidorComponent;
  let fixture: ComponentFixture<LoginServidorComponent>;

  beforeEach(() => {
    TestBed.configureTestingModule({
      declarations: [LoginServidorComponent]
    });
    fixture = TestBed.createComponent(LoginServidorComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
