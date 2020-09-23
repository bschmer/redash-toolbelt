import click
import client
import pprint
import pdb


@click.command()
@click.option('--redash-url')
@click.option('--api-key', help="API Key")
@click.option('--dashboard-slug', help="Dashboard slug")
def main(redash_url, api_key, dashboard_slug):
    redash_client = client.Redash(redash_url, api_key)
    redash_client.duplicate_dashboard(dashboard_slug)
    '''
    dashboard = redash_client.dashboard(dashboard_slug)


    for widget in dashboard['widgets']:
        pprint.pprint(widget)
    value = redash_client.query(439853)
    data = value.json()
    print data
    print redash_client.duplicate_query(477642)
    '''


if __name__ == '__main__':
    main()
