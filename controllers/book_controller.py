from flask import Flask, render_template, Blueprint, request, redirect
from repositories import book_repository
from repositories import author_repository