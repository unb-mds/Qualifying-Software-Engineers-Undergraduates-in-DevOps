---
layout: page
title: Aulas
permalink: /aulas/
---

<div class="aulas-page">
  <div class="aulas-header">
    <h1><i class="fas fa-chalkboard-teacher"></i> Cronograma de Aulas</h1>
    <p>Confira abaixo o cronograma completo das aulas e eventos da disciplina MDS 2026/1.</p>
  </div>

  <div class="aulas-list">
    {% assign sorted_events = site.events | sort: 'order' %}
    {% assign aula_counter = 0 %}
    {% for event in sorted_events %}
    {% if event.type == 'lecture' %}
      {% assign aula_counter = aula_counter | plus: 1 %}
    {% endif %}
    <div class="aula-card {% if event.type == 'lecture' %}lecture{% elsif event.type == 'review' %}review{% elsif event.type == 'release' %}release{% else %}other{% endif %}">
      <div class="aula-date">
        {% if event.type == 'lecture' %}
        <span class="day">{{ aula_counter | prepend: '0' | slice: -2, 2 }}</span>
        <span class="month">Aula</span>
        {% else %}
        <span class="day">{{ event.date | date: "%d" }}</span>
        <span class="month">{{ event.date | date: "%b" }}</span>
        {% endif %}
      </div>
      <div class="aula-content">
        <h3 class="aula-title">{{ event.name }}</h3>
        {% if event.description %}
        <p class="aula-description">{{ event.description }}</p>
        {% endif %}
        {% if event.links %}
        <div class="aula-links">
          {% for link in event.links %}
          <a href="{{ link.url }}" target="_blank" class="aula-link">
            <i class="fas fa-play-circle"></i> {{ link.name }}
          </a>
          {% endfor %}
        </div>
        {% endif %}
        {% if event.hide_from_anno498uncements != true %}
        <span class="aula-type">
          {% if event.type == 'lecture' %}
            <i class="fas fa-book"></i> Aula
          {% elsif event.type == 'review' %}
            <i class="fas fa-users"></i> Review
          {% elsif event.type == 'release' %}
            <i class="fas fa-rocket"></i> Release
          {% else %}
            <i class="fas fa-calendar"></i> Evento
          {% endif %}
        </span>
        {% endif %}
      </div>
    </div>
    {% endfor %}
  </div>
</div>

<style>
.aulas-page {
  max-width: 900px;
  margin: 0 auto;
}

.aulas-header {
  text-align: center;
  margin-bottom: 2rem;
  padding: 2rem;
  background: linear-gradient(135deg, #FF8E53 0%, #FF6B6B 100%);
  color: white;
  border-radius: 12px;
}

.aulas-header h1 {
  margin: 0 0 0.5rem 0;
  font-size: 2rem;
}

.aulas-header p {
  margin: 0;
  opacity: 0.9;
}

.aulas-list {
  display: flex;
  flex-direction: column;
  gap: 1rem;
}

.aula-card {
  display: flex;
  gap: 1.5rem;
  padding: 1.25rem;
  background: white;
  border: 1px solid #e1e1e1;
  border-radius: 8px;
  transition: all 0.2s ease;
  border-left: 4px solid #667eea;
}

.aula-card:hover {
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.08);
  transform: translateX(4px);
}

.aula-card.lecture {
  border-left-color: #FF8E53;
}

.aula-card.review {
  border-left-color: #4ECDC4;
}

.aula-card.release {
  border-left-color: #e74c3c;
}

.aula-card.other {
  border-left-color: #95a5a6;
}

.aula-date {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  min-width: 60px;
  padding: 0.5rem;
  background: #f5f5f5;
  border-radius: 8px;
}

.aula-date .day {
  font-size: 1.5rem;
  font-weight: 700;
  color: #1f1f1f;
  line-height: 1;
}

.aula-date .month {
  font-size: 0.85rem;
  color: #636363;
  text-transform: uppercase;
}

.aula-content {
  flex: 1;
}

.aula-title {
  margin: 0 0 0.5rem 0;
  font-size: 1.1rem;
  font-weight: 600;
  color: #1f1f1f;
}

.aula-description {
  margin: 0 0 0.75rem 0;
  color: #636363;
  font-size: 0.9rem;
  line-height: 1.5;
}

.aula-type {
  display: inline-flex;
  align-items: center;
  gap: 0.25rem;
  font-size: 0.8rem;
  color: #636363;
  background: #f5f5f5;
  padding: 0.25rem 0.75rem;
  border-radius: 12px;
}

.aula-type i {
  font-size: 0.75rem;
}

.aula-links {
  display: flex;
  flex-wrap: wrap;
  gap: 0.5rem;
  margin-bottom: 0.75rem;
}

.aula-link {
  display: inline-flex;
  align-items: center;
  gap: 0.35rem;
  font-size: 0.85rem;
  color: #FF6B6B;
  text-decoration: none;
  padding: 0.35rem 0.75rem;
  background: rgba(255, 107, 107, 0.1);
  border-radius: 6px;
  transition: all 0.2s ease;
}

.aula-link:hover {
  background: #FF6B6B;
  color: white;
  text-decoration: none;
}

.aula-link i {
  font-size: 0.8rem;
}

@media (max-width: 576px) {
  .aulas-header {
    padding: 1.5rem 1rem;
  }
  
  .aulas-header h1 {
    font-size: 1.5rem;
  }
  
  .aula-card {
    flex-direction: column;
    gap: 1rem;
  }
  
  .aula-date {
    flex-direction: row;
    gap: 0.5rem;
    width: fit-content;
  }
  
  .aula-date .day {
    font-size: 1.25rem;
  }
}
</style>
