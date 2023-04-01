from django.db.models import Q, Sum, IntegerField

from stats.models import Income, Outcome


queries = {
    'jan': Sum('value', distinct=True, filter=Q(month=1), output_field=IntegerField()),
    'feb': Sum('value', distinct=True, filter=Q(month=2), output_field=IntegerField()),
    'mar': Sum('value', distinct=True, filter=Q(month=3), output_field=IntegerField()),
    'apr': Sum('value', distinct=True, filter=Q(month=4), output_field=IntegerField()),
    'may': Sum('value', distinct=True, filter=Q(month=5), output_field=IntegerField()),
    'jun': Sum('value', distinct=True, filter=Q(month=6), output_field=IntegerField()),
    'jul': Sum('value', distinct=True, filter=Q(month=7), output_field=IntegerField()),
    'aug': Sum('value', distinct=True, filter=Q(month=8), output_field=IntegerField()),
    'sep': Sum('value', distinct=True, filter=Q(month=9), output_field=IntegerField()),
    'oct': Sum('value', distinct=True, filter=Q(month=10), output_field=IntegerField()),
    'now': Sum('value', distinct=True, filter=Q(month=11), output_field=IntegerField()),
    'dec': Sum('value', distinct=True, filter=Q(month=12), output_field=IntegerField()),
}


def get_stats(filters):
    stats_income = Income.objects.filter(**filters).aggregate(**queries, 
        by_year=Sum('value', distinct=True, output_field=IntegerField()),
        )
    stats_outcome = Outcome.objects.filter(**filters).aggregate(**queries, 
        by_year=Sum('value', distinct=True, output_field=IntegerField()),
        )

    data = []
    for key, val in stats_income.items():
        if key == 'by_year':
            continue
        dt = {'profit': stats_income[key] or 0, 'loss': stats_outcome[key] or 0}
        data.append(dt)
    
    res = {
        'by_month': data,
        'by_year': {
            'profit': stats_income['by_year'] or 0, 
            'loss': stats_outcome['by_year'] or 0
            } 
    }

    return res
