.class public Lcom/example/myapplication/Test02;
.super Landroidx/appcompat/app/AppCompatActivity;
.source "Test02.java"


# direct methods
.method public constructor <init>()V
    .locals 0

    .line 7
    invoke-direct {p0}, Landroidx/appcompat/app/AppCompatActivity;-><init>()V

    return-void
.end method


# virtual methods
.method protected onCreate(Landroid/os/Bundle;)V
    .locals 0

    .line 11
    invoke-super {p0, p1}, Landroidx/appcompat/app/AppCompatActivity;->onCreate(Landroid/os/Bundle;)V

    const p1, 0x7f09001e

    .line 12
    invoke-virtual {p0, p1}, Lcom/example/myapplication/Test02;->setContentView(I)V

    return-void
.end method
